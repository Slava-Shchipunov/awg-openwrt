#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AwgOpt:
    name: str
    kind: str
    placeholder: str | None
    description: str

    @property
    def lower(self) -> str:
        return self.name.lower()

    @property
    def uci(self) -> str:
        return f"awg_{self.lower}"

    @property
    def proto_config_type(self) -> str:
        return self.kind

    @property
    def luci_datatype(self) -> str:
        if self.kind == "int":
            return "uinteger"

        return "string"


AWG_OPTS = [
    AwgOpt("Jc", "int", "4", "Junk packet count, 0-10."),
    AwgOpt("Jmin", "int", "64", "Junk packet minimum size, 64-1024 bytes."),
    AwgOpt("Jmax", "int", "205", "Junk packet maximum size, 64-1024 bytes."),
    AwgOpt(
        "S1",
        "int",
        "56",
        "Handshake initiation random prefix size, 0-64 bytes.",
    ),
    AwgOpt(
        "S2",
        "int",
        "48",
        "Handshake response random prefix size, 0-64 bytes.",
    ),
    AwgOpt(
        "S3",
        "int",
        "32",
        "Cookie reply random prefix size, 0-64 bytes.",
    ),
    AwgOpt(
        "S4",
        "int",
        "16",
        "Transport packet random prefix size, 0-32 bytes.",
    ),
    AwgOpt(
        "H1",
        "string",
        "135792468-135903579",
        "Handshake initiation packet type header. "
        "Number or range, 0-4294967295. "
        "H1-H4 ranges must not overlap.",
    ),
    AwgOpt(
        "H2",
        "string",
        "864201357-864312468",
        "Handshake response packet type header. "
        "Number or range, 0-4294967295. "
        "H1-H4 ranges must not overlap.",
    ),
    AwgOpt(
        "H3",
        "string",
        "2198765432-2198876543",
        "Handshake cookie packet type header. "
        "Number or range, 0-4294967295. "
        "H1-H4 ranges must not overlap.",
    ),
    AwgOpt(
        "H4",
        "string",
        "4012345678-4012456789",
        "Transport packet type header. "
        "Number or range, 0-4294967295. "
        "H1-H4 ranges must not overlap.",
    ),
    AwgOpt("I1", "string", "<r 128>", "First special junk packet signature."),
    AwgOpt("I2", "string", None, "Second special junk packet signature."),
    AwgOpt("I3", "string", None, "Third special junk packet signature."),
    AwgOpt("I4", "string", None, "Fourth special junk packet signature."),
    AwgOpt("I5", "string", None, "Fifth special junk packet signature."),
]


AWG_TOOLS_VERSION = "1.0.20260223"
AWG_LUCI_VERSION = "2.2.0"
AWG_MAINTAINER = "Amnezia Admin <admin@amnezia.org>"
AWG_LUCI_MK_INCLUDE = "include $(TOPDIR)/feeds/luci/luci.mk"


OPENWRT_REPO = os.environ.get(
    "OPENWRT_REPO",
    "https://github.com/openwrt/openwrt.git",
)
OPENWRT_REF = os.environ.get("OPENWRT_REF", "openwrt-25.12")
OPENWRT_WG_TOOLS_DIR = "package/network/utils/wireguard-tools"

LUCI_REPO = os.environ.get(
    "LUCI_REPO",
    "https://github.com/openwrt/luci.git",
)
LUCI_REF = os.environ.get("LUCI_REF", "openwrt-25.12")
LUCI_WG_PROTO_DIR = "protocols/luci-proto-wireguard"

AWG_TOOLS_DIR = Path("amneziawg-tools")
AWG_FILES_DIR = AWG_TOOLS_DIR / "files"
AWG_TOOLS_PROTO_FILE = AWG_FILES_DIR / "amneziawg.sh"

AWG_LUCI_DIR = Path("luci-proto-amneziawg")
AWG_LUCI_PROTO_FILE = (
    AWG_LUCI_DIR / "htdocs/luci-static/resources/protocol/amneziawg.js"
)
AWG_LUCI_ICON_FILE = AWG_LUCI_DIR / "htdocs/luci-static/resources/icons/amneziawg.svg"

OPENWRT_SRC_DIR = Path(".openwrt-wg-src")
LUCI_SRC_DIR = Path(".luci-proto-wireguard-src")


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)


def rm_rf(path: Path) -> None:
    if not path.exists() and not path.is_symlink():
        return

    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink()


def sparse_checkout(
    work_dir: Path,
    repo: str,
    ref: str,
    sparse_dir: str,
) -> None:
    rm_rf(work_dir)
    work_dir.mkdir(parents=True)

    run(["git", "-C", str(work_dir), "init", "-q"])
    run(["git", "-C", str(work_dir), "remote", "add", "origin", repo])
    run(["git", "-C", str(work_dir), "sparse-checkout", "init", "--cone"])
    run(["git", "-C", str(work_dir), "sparse-checkout", "set", sparse_dir])
    run(["git", "-C", str(work_dir), "fetch", "--depth=1", "origin", ref])
    run(["git", "-C", str(work_dir), "checkout", "-q", "--detach", "FETCH_HEAD"])


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def try_read_utf8(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def is_svg(path: Path) -> bool:
    return path.suffix.lower() == ".svg"


def save_file(path: Path) -> bytes | None:
    if not path.exists():
        return None

    return path.read_bytes()


def restore_file(path: Path, data: bytes | None) -> None:
    if data is None:
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def insert_after_line(path: Path, marker_regex: str, block: str) -> None:
    lines = read_text(path).splitlines(keepends=True)

    for index, line in enumerate(lines):
        if re.search(marker_regex, line):
            if not block.endswith("\n"):
                block += "\n"

            lines.insert(index + 1, block)
            write_text(path, "".join(lines))
            return

    raise RuntimeError(f"marker not found in {path}: {marker_regex}")


def replace_call_block(path: Path, start_regex: str, block: str) -> None:
    lines = read_text(path).splitlines(keepends=True)
    start_index = None
    end_index = None

    for index, line in enumerate(lines):
        if start_index is None:
            if re.search(start_regex, line):
                start_index = index

                if ");" in line:
                    end_index = index
                    break

            continue

        if ");" in line:
            end_index = index
            break

    if start_index is None:
        raise RuntimeError(f"start marker not found in {path}: {start_regex}")

    if end_index is None:
        raise RuntimeError(f"end of call not found in {path}: {start_regex}")

    if not block.endswith("\n"):
        block += "\n"

    new_lines = lines[:start_index] + [block] + lines[end_index + 1 :]
    write_text(path, "".join(new_lines))


def rewrite_text_tree(root: Path, transform, skip_path=None) -> None:
    for path in root.rglob("*"):
        if not path.is_file():
            continue

        if skip_path is not None and skip_path(path):
            continue

        text = try_read_utf8(path)
        if text is None:
            continue

        new_text = transform(text)

        if new_text != text:
            write_text(path, new_text)


def rename_path(old: Path, new: Path) -> None:
    if not old.exists():
        raise RuntimeError(f"path not found: {old}")

    new.parent.mkdir(parents=True, exist_ok=True)
    old.rename(new)


def rename_wg_to_awg_text(text: str, *, replace_wg0_conf: bool) -> str:
    text = text.replace("Wg", "Awg")
    text = text.replace("WG", "AWG")
    text = re.sub(r"\bwg\b", "awg", text)
    text = re.sub(r"(^|[^a])wg_", r"\1awg_", text, flags=re.MULTILINE)

    if replace_wg0_conf:
        text = text.replace("wg0.conf", "awg0.conf")

    text = text.replace("wireguard", "amneziawg")
    text = text.replace("WireGuard", "AmneziaWG")
    text = text.replace("Wireguard", "AmneziaWG")

    return text


def trim_makefile_before_rules(path: Path) -> str:
    text = read_text(path)
    include_marker = "include $(TOPDIR)/rules.mk"
    include_index = text.find(include_marker)

    if include_index < 0:
        raise RuntimeError(f"include marker not found in {path}: {include_marker}")

    return text[include_index:]


def update_tools_makefile(path: Path) -> None:
    text = trim_makefile_before_rules(path)

    lines = text.splitlines()
    new_lines: list[str] = []
    inserted_source = False
    skip_prefixes = (
        "PKG_SOURCE:=",
        "PKG_SOURCE_URL:=",
        "PKG_HASH:=",
        "PKG_MIRROR_HASH:=",
        "PKG_SOURCE_PROTO:=",
        "PKG_SOURCE_VERSION:=",
        "PKG_SOURCE_DATE:=",
    )

    for line in lines:
        if line.startswith("PKG_VERSION:="):
            new_lines.append(f"PKG_VERSION:={AWG_TOOLS_VERSION}")
            continue

        if line.startswith("PKG_RELEASE:="):
            new_lines.extend(
                [
                    "PKG_RELEASE:=1",
                    "",
                    "PKG_SOURCE_PROTO:=git",
                    "PKG_SOURCE_URL:=https://github.com/amnezia-vpn/amneziawg-tools.git",
                    "PKG_SOURCE_VERSION:=v$(PKG_VERSION)",
                ]
            )
            inserted_source = True
            continue

        if line.startswith(skip_prefixes):
            continue

        new_lines.append(line)

    if not inserted_source:
        raise RuntimeError(f"PKG_RELEASE marker not found in {path}")

    text = "\n".join(new_lines) + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(
        r"^(\s*URL:=).*$",
        r"\1https://amnezia.org/",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^(\s*MAINTAINER:=).*$",
        rf"\1{AWG_MAINTAINER}",
        text,
        flags=re.MULTILINE,
    )

    write_text(path, text)


def fix_tools_install_binary_name(path: Path) -> None:
    text = read_text(path)

    old = "\t$(INSTALL_BIN) $(PKG_BUILD_DIR)/src/awg $(1)/usr/bin/"
    new = "\t$(INSTALL_BIN) $(PKG_BUILD_DIR)/src/wg $(1)/usr/bin/awg"

    if new in text:
        return

    if old not in text:
        raise RuntimeError(f"install binary line not found in {path}")

    write_text(path, text.replace(old, new, 1))


def rewrite_luci_mk_include(text: str) -> str:
    old = "include ../../luci.mk"

    if old not in text:
        raise RuntimeError("luci.mk include marker not found")

    return text.replace(old, AWG_LUCI_MK_INCLUDE, 1)


def update_luci_makefile(path: Path) -> None:
    text = trim_makefile_before_rules(path)
    text = rewrite_luci_mk_include(text)

    if AWG_LUCI_MK_INCLUDE not in text:
        raise RuntimeError(f"luci.mk include was not rewritten in {path}")

    version_line = f"PKG_VERSION:={AWG_LUCI_VERSION}"

    if re.search(r"^PKG_VERSION:=", text, flags=re.MULTILINE):
        text = re.sub(
            r"^PKG_VERSION:=.*$",
            version_line,
            text,
            flags=re.MULTILINE,
        )
    else:
        text = text.replace(
            "include $(TOPDIR)/rules.mk\n",
            f"include $(TOPDIR)/rules.mk\n\n{version_line}\n",
            1,
        )

    text = re.sub(
        r"^PKG_MAINTAINER:=.*$",
        f"PKG_MAINTAINER:={AWG_MAINTAINER}",
        text,
        flags=re.MULTILINE,
    )

    if version_line not in text:
        raise RuntimeError(f"PKG_VERSION marker not added in {path}")

    if f"PKG_MAINTAINER:={AWG_MAINTAINER}" not in text:
        raise RuntimeError(f"PKG_MAINTAINER marker not found in {path}")

    write_text(path, text)


def js_quote(text: str) -> str:
    return text.replace("\\", "\\\\").replace("'", "\\'")


def gen_tools_proto_config_adds() -> str:
    lines = [
        "",
        "\t# AmneziaWG specific parameters",
    ]

    for opt in AWG_OPTS:
        line = f'\tproto_config_add_{opt.proto_config_type} "{opt.uci}"'
        lines.append(line)

    return "\n".join(lines) + "\n"


def gen_tools_local_vars() -> str:
    lines = [
        "",
        "\t# AmneziaWG specific parameters",
    ]

    for opt in AWG_OPTS:
        lines.append(f"\tlocal {opt.uci}")

    lines.append("")
    return "\n".join(lines) + "\n"


def gen_tools_config_gets() -> str:
    lines = [
        "",
        "\t# AmneziaWG specific parameters",
    ]

    for opt in AWG_OPTS:
        lines.append(f'\tconfig_get {opt.uci} "${{config}}" "{opt.uci}"')

    return "\n".join(lines) + "\n"


def gen_tools_awg_config_lines() -> str:
    lines = [
        "",
        "\t# AmneziaWG specific parameters",
    ]

    for opt in AWG_OPTS:
        lines.append(
            f'\t[ -n "${{{opt.uci}}}" ] && '
            f'awg_config="${{awg_config}}{opt.name}=${{{opt.uci}}}\\n"'
        )

    return "\n".join(lines) + "\n"


def gen_luci_settings_tab() -> str:
    doc_html = (
        "_('Further information about AmneziaWG interfaces and peers at ' + "
        "'<a href=\\'https://docs.amnezia.org/documentation/amnezia-wg\\'>"
        "amnezia.org</a>.')"
    )

    lines = [
        "",
        "\t\t// AmneziaWG specific parameters",
        "\t\ttry {",
        ("\t\t\ts.tab('amneziawg', _('AmneziaWG Settings'), " f"{doc_html});"),
        "\t\t}",
        "\t\tcatch(e) {}",
    ]

    for opt in AWG_OPTS:
        lines.extend(
            [
                "",
                (
                    "\t\to = s.taboption('amneziawg', form.Value, "
                    f"'{opt.uci}', _('{js_quote(opt.name)}'), "
                    f"_('{js_quote(opt.description)}'));"
                ),
                f"\t\to.datatype = '{opt.luci_datatype}';",
            ]
        )

        if opt.placeholder is not None:
            lines.append(f"\t\to.placeholder = '{js_quote(opt.placeholder)}';")

        lines.append("\t\to.optional = true;")

    return "\n".join(lines) + "\n"


def gen_luci_peers_tab() -> str:
    doc_html = (
        "_('Further information about AmneziaWG interfaces and peers at ' + "
        "'<a href=\\'https://docs.amnezia.org/documentation/amnezia-wg\\'>"
        "amnezia.org</a>.')"
    )

    lines = [
        f"\t\t\ts.tab('peers', _('Peers'), {doc_html});",
    ]

    return "\n".join(lines) + "\n"


def gen_luci_import_setters() -> str:
    lines = [
        "",
        "\t\t\t\t\t// AmneziaWG specific parameters",
    ]

    for opt in AWG_OPTS:
        lines.append(
            f"\t\t\t\t\ts.getOption('{opt.uci}')"
            f".getUIElement(s.section)"
            f".setValue(config.interface_{opt.lower} || '');"
        )

    return "\n".join(lines) + "\n"


def gen_luci_export_vars() -> str:
    lines = [
        "",
        "\t\t\t// AmneziaWG specific parameters",
    ]

    for opt in AWG_OPTS:
        lines.append(
            f"\t\t\tconst {opt.lower} = " f"s.formvalue(s.section, '{opt.uci}');"
        )

    return "\n".join(lines) + "\n"


def gen_luci_export_lines() -> str:
    lines = [
        "\t\t\t\t// AmneziaWG specific parameters",
    ]

    for opt in AWG_OPTS:
        lines.append(
            f"\t\t\t\t{opt.lower} ? "
            f"'{opt.name} = ' + {opt.lower} : "
            f"'# {opt.name} not defined',"
        )

    return "\n".join(lines) + "\n"


def make_qr_generation_defensive(path: Path) -> None:
    start_re = re.compile(r"const svg = uqr\.renderSVG\(data, options\);")
    end_re = re.compile(r"dom\.content\(code, Object\.assign\(E\(svg\)")

    lines = read_text(path).splitlines(keepends=True)
    start_index = None
    end_index = None

    for index, line in enumerate(lines):
        if start_index is None and start_re.search(line):
            start_index = index

        if start_index is not None and end_re.search(line):
            end_index = index
            break

    if start_index is None:
        raise RuntimeError(f"QR start marker not found in {path}")

    if end_index is None:
        raise RuntimeError(f"QR end marker not found in {path}")

    before = lines[:start_index]
    body = ["\t" + line for line in lines[start_index : end_index + 1]]
    after = lines[end_index + 1 :]

    try_block = [
        "\n",
        "\t// Large configurations may exceed QR code size limits.\n",
        "\ttry {\n",
    ]

    qr_error = "QR code generation failed. The configuration may be too large."
    catch_block = [
        "\t} catch (e) {\n",
        "\t\tconsole.warn('QR generation failed:', e);\n",
        "\n",
        "\t\tcode.style.opacity = '';\n",
        (
            "\t\tdom.content(code, E('div', "
            "{'class': 'alert-message warning', "
            "'style': 'margin:0;text-align:center'}, "
            f"[_('{qr_error}')]));\n"
        ),
        "\t}\n",
    ]

    write_text(path, "".join(before + try_block + body + catch_block + after))


def update_tools(*, rename_only: bool) -> None:
    print("Fetching WireGuard tools package from OpenWrt:")
    print(f"  repo: {OPENWRT_REPO}")
    print(f"  ref:  {OPENWRT_REF}")
    print(f"  dir:  {OPENWRT_WG_TOOLS_DIR}")

    sparse_checkout(
        OPENWRT_SRC_DIR,
        OPENWRT_REPO,
        OPENWRT_REF,
        OPENWRT_WG_TOOLS_DIR,
    )

    rm_rf(AWG_TOOLS_DIR)

    shutil.copytree(
        OPENWRT_SRC_DIR / OPENWRT_WG_TOOLS_DIR,
        AWG_TOOLS_DIR,
    )

    rm_rf(OPENWRT_SRC_DIR)

    rename_path(
        AWG_FILES_DIR / "wireguard_watchdog",
        AWG_FILES_DIR / "amneziawg_watchdog",
    )

    rename_path(
        AWG_FILES_DIR / "wireguard.sh",
        AWG_TOOLS_PROTO_FILE,
    )

    if rename_only:
        print("Updated rename-only vanilla tree:")
        print(f"  {AWG_TOOLS_DIR}")
        return

    rewrite_text_tree(
        AWG_TOOLS_DIR,
        lambda text: rename_wg_to_awg_text(
            text,
            replace_wg0_conf=False,
        ),
        skip_path=is_svg,
    )

    update_tools_makefile(AWG_TOOLS_DIR / "Makefile")
    fix_tools_install_binary_name(AWG_TOOLS_DIR / "Makefile")

    insert_after_line(
        AWG_TOOLS_PROTO_FILE,
        r'proto_config_add_string "addresses"',
        gen_tools_proto_config_adds(),
    )

    insert_after_line(
        AWG_TOOLS_PROTO_FILE,
        r"local private_key listen_port mtu fwmark "
        r"addresses ip6prefix nohostroute tunlink",
        gen_tools_local_vars(),
    )

    insert_after_line(
        AWG_TOOLS_PROTO_FILE,
        r'config_get tunlink "\$\{config\}" "tunlink"',
        gen_tools_config_gets(),
    )

    insert_after_line(
        AWG_TOOLS_PROTO_FILE,
        r'FwMark=\$\{fwmark\}\\n"',
        gen_tools_awg_config_lines(),
    )

    print("Updated:")
    print(f"  {AWG_TOOLS_DIR}")


def update_luci(*, rename_only: bool) -> None:
    print("Fetching LuCI WireGuard protocol package from:")
    print(f"  repo: {LUCI_REPO}")
    print(f"  ref:  {LUCI_REF}")
    print(f"  dir:  {LUCI_WG_PROTO_DIR}")

    sparse_checkout(
        LUCI_SRC_DIR,
        LUCI_REPO,
        LUCI_REF,
        LUCI_WG_PROTO_DIR,
    )

    saved_awg_svg = save_file(AWG_LUCI_ICON_FILE)

    rm_rf(AWG_LUCI_DIR)

    shutil.copytree(
        LUCI_SRC_DIR / LUCI_WG_PROTO_DIR,
        AWG_LUCI_DIR,
    )

    restore_file(AWG_LUCI_ICON_FILE, saved_awg_svg)
    rm_rf(LUCI_SRC_DIR)

    rename_path(
        AWG_LUCI_DIR / "htdocs/luci-static/resources/protocol/wireguard.js",
        AWG_LUCI_PROTO_FILE,
    )

    rename_path(
        AWG_LUCI_DIR / "htdocs/luci-static/resources/view/wireguard",
        AWG_LUCI_DIR / "htdocs/luci-static/resources/view/amneziawg",
    )

    rename_path(
        AWG_LUCI_DIR / "root/usr/share/luci/menu.d/luci-proto-wireguard.json",
        AWG_LUCI_DIR / "root/usr/share/luci/menu.d/luci-proto-amneziawg.json",
    )

    rename_path(
        AWG_LUCI_DIR / "root/usr/share/rpcd/ucode/luci.wireguard",
        AWG_LUCI_DIR / "root/usr/share/rpcd/ucode/luci.amneziawg",
    )

    rename_path(
        AWG_LUCI_DIR / "root/usr/share/rpcd/acl.d/luci-wireguard.json",
        AWG_LUCI_DIR / "root/usr/share/rpcd/acl.d/luci-amneziawg.json",
    )

    if rename_only:
        print("Updated rename-only vanilla tree:")
        print(f"  {AWG_LUCI_DIR}")
        return

    rewrite_text_tree(
        AWG_LUCI_DIR,
        lambda text: rename_wg_to_awg_text(
            text,
            replace_wg0_conf=True,
        ),
        skip_path=is_svg,
    )

    update_luci_makefile(AWG_LUCI_DIR / "Makefile")

    insert_after_line(
        AWG_LUCI_PROTO_FILE,
        r"o\.datatype = 'cidr6';",
        gen_luci_settings_tab(),
    )

    replace_call_block(
        AWG_LUCI_PROTO_FILE,
        r"s\.tab\('peers'",
        gen_luci_peers_tab(),
    )

    insert_after_line(
        AWG_LUCI_PROTO_FILE,
        r"s\.getOption\('addresses'\)\.getUIElement\(s\.section\)",
        gen_luci_import_setters(),
    )

    insert_after_line(
        AWG_LUCI_PROTO_FILE,
        r"s\.formvalue\(s\.section, 'listen_port'\) \|\| '51820';",
        gen_luci_export_vars(),
    )

    insert_after_line(
        AWG_LUCI_PROTO_FILE,
        r"dns && dns\.length .*'DNS = '.*'# DNS not defined',",
        gen_luci_export_lines(),
    )

    make_qr_generation_defensive(AWG_LUCI_PROTO_FILE)

    print("Updated:")
    print(f"  {AWG_LUCI_DIR}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update amneziawg-tools and luci-proto-amneziawg."
    )

    parser.add_argument(
        "target",
        nargs="?",
        choices=("tools", "luci", "all"),
        default="all",
        help="what to update",
    )

    parser.add_argument(
        "--rename-only",
        action="store_true",
        help="copy upstream packages and rename paths only",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.target in ("tools", "all"):
        update_tools(rename_only=args.rename_only)

    if args.target in ("luci", "all"):
        update_luci(rename_only=args.rename_only)


if __name__ == "__main__":
    main()
