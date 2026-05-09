(function () {
  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }

    var textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.setAttribute('readonly', '');
    textarea.style.position = 'absolute';
    textarea.style.left = '-9999px';
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    return Promise.resolve();
  }

  function enhanceCodeBlocks() {
    document.querySelectorAll('pre').forEach(function (pre) {
      if (pre.dataset.copyEnhanced === 'true') {
        return;
      }

      var code = pre.querySelector('code');
      if (!code) {
        return;
      }

      pre.dataset.copyEnhanced = 'true';
      pre.style.position = 'relative';

      var button = document.createElement('button');
      button.type = 'button';
      button.textContent = 'Copy';
      button.setAttribute('aria-label', 'Copy code');
      button.style.position = 'absolute';
      button.style.top = '0.5rem';
      button.style.right = '0.5rem';
      button.style.padding = '0.25rem 0.5rem';
      button.style.border = '1px solid rgba(255,255,255,0.35)';
      button.style.borderRadius = '4px';
      button.style.background = 'rgba(0,0,0,0.45)';
      button.style.color = '#fff';
      button.style.cursor = 'pointer';
      button.style.fontSize = '0.75rem';

      button.addEventListener('click', function () {
        copyText(code.innerText).then(function () {
          button.textContent = 'Copied';
          window.setTimeout(function () {
            button.textContent = 'Copy';
          }, 1200);
        });
      });

      pre.appendChild(button);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', enhanceCodeBlocks);
  } else {
    enhanceCodeBlocks();
  }
}());
