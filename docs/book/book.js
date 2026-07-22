// 알짜 파이썬 웹 본문 — 인터랙션 (DESIGN.md 기반)
// 1) 스크롤 리빌  2) 그림 클릭 → 별도 창 확대 보기  3) 코드 복사 버튼

// ---- 1) 스크롤 리빌 ----
(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var targets = document.querySelectorAll(
    '.content figure.fig, .content .box, .content .listing, ' +
    '.content .table-wrap, .content pre.line-numbers, ' +
    '.content pre.pyout, .content pre.termout, .cover-wrap');
  targets.forEach(function (el) { el.classList.add('reveal'); });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -5% 0px' });
  targets.forEach(function (el) { io.observe(el); });
})();

// ---- 1.5) 사이드바 링크 클릭 시 모바일 목차 서랍 닫기 ----
// 절(#anchor) 링크는 페이지 이동이 없어 서랍이 열린 채 본문을 가리는 문제 방지
(function () {
  document.querySelectorAll('.sidebar a').forEach(function (a) {
    a.addEventListener('click', function () {
      document.body.classList.remove('nav-open');
    });
  });
})();

// ---- 2) 그림 클릭 → 별도 창 확대 ----
(function () {
  var imgs = document.querySelectorAll(
    '.content img.tikz, .content img.gfx, .content img.shot, ' +
    '.content img.chapfig, .content img.cover');
  imgs.forEach(function (img) {
    img.classList.add('zoomable');
    img.title = '클릭하면 새 창에서 크게 볼 수 있습니다';
    img.addEventListener('click', function () {
      var src = img.getAttribute('src');
      var w = Math.min(window.screen.availWidth, 1280);
      var h = Math.min(window.screen.availHeight, 900);
      window.open('viewer.html?src=' + encodeURIComponent(src),
        'figviewer', 'width=' + w + ',height=' + h +
        ',menubar=no,toolbar=no,location=no,status=no');
    });
  });
})();

// ---- 3) 코드 복사 버튼 (행번호 제외) ----
(function () {
  var COPY_ICON =
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" ' +
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" ' +
    'stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" ' +
    'rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 ' +
    '2-2h9a2 2 0 0 1 2 2v1"></path></svg>';
  var OK_ICON =
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" ' +
    'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" ' +
    'stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>';

  document.querySelectorAll('.content pre.line-numbers').forEach(function (pre) {
    var codeEl = pre.querySelector('code');
    if (!codeEl) return;
    var wrap = document.createElement('div');
    wrap.className = 'code-wrap';
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);
    var btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.type = 'button';
    btn.title = '코드 복사 (행번호 제외)';
    btn.innerHTML = COPY_ICON + '<span>복사</span>';
    wrap.appendChild(btn);
    btn.addEventListener('click', function () {
      // Prism 토큰만 담긴 code 요소의 textContent에는 행번호가 포함되지 않음
      var text = codeEl.textContent.replace(/\n$/, '');
      function done(ok) {
        btn.innerHTML = ok ? OK_ICON + '<span>복사됨</span>'
                           : COPY_ICON + '<span>실패</span>';
        btn.classList.toggle('ok', ok);
        setTimeout(function () {
          btn.innerHTML = COPY_ICON + '<span>복사</span>';
          btn.classList.remove('ok');
        }, 1600);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(
          function () { done(true); }, function () { done(false); });
      } else {
        var ta = document.createElement('textarea');
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        var ok = false;
        try { ok = document.execCommand('copy'); } catch (e) {}
        document.body.removeChild(ta);
        done(ok);
      }
    });
  });
})();
