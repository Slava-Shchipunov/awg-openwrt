(function () {
  function copyText(text) {
    return navigator.clipboard.writeText(text);
  }

  function enhanceCodeBlocks() {
    document.querySelectorAll('pre').forEach(function (pre) {
      const code = pre.querySelector('code');
      if (!code) {
        return;
      }

      let wrapper = pre.parentElement;
      if (!wrapper || !wrapper.classList.contains('highlight')) {
        wrapper = document.createElement('div');
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);
      }

      if (wrapper.dataset.copyEnhanced === 'true') {
        return;
      }

      wrapper.dataset.copyEnhanced = 'true';
      wrapper.style.position = 'relative';
      pre.style.position = '';

      const button = document.createElement('button');
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
        }).catch(function () {
          button.textContent = 'Failed';
          window.setTimeout(function () {
            button.textContent = 'Copy';
          }, 1200);
        });
      });

      wrapper.appendChild(button);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', enhanceCodeBlocks);
  } else {
    enhanceCodeBlocks();
  }
}());
