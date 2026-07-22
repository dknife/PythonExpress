// 알짜 파이썬 웹 본문 — 스크롤 리빌 (DESIGN.md: 뷰포트 진입 시 페이드인)
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
