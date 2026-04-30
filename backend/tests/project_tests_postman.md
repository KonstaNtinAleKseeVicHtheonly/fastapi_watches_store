<!DOCTYPE html>
<!-- saved from url=(0078)https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-css-features="prs_sticky_header_top_fix" data-darkreader-mode="dynamic" data-darkreader-scheme="dark" data-darkreader-proxy-injected="true" class="js-focus-visible" data-js-focus-visible="" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style><style class="darkreader darkreader--sync" media="screen"></style><style class="darkreader darkreader--fallback" media="screen"></style><style class="darkreader darkreader--user-agent" media="screen">@layer {
html {
    background-color: var(--darkreader-background-ffffff, #181a1b) !important;
}
html {
    color-scheme: dark !important;
}
iframe {
    color-scheme: dark !important;
}
html, body {
    background-color: var(--darkreader-background-ffffff, #181a1b);
}
html, body {
    border-color: var(--darkreader-border-4c4c4c, #736b5e);
    color: var(--darkreader-text-000000, #e8e6e3);
}
a {
    color: var(--darkreader-text-0040ff, #3391ff);
}
table {
    border-color: var(--darkreader-border-808080, #545b5e);
}
mark {
    color: var(--darkreader-text-000000, #e8e6e3);
}
::placeholder {
    color: var(--darkreader-text-a9a9a9, #b2aba1);
}
input:-webkit-autofill,
textarea:-webkit-autofill,
select:-webkit-autofill {
    background-color: var(--darkreader-background-faffbd, #404400) !important;
    color: var(--darkreader-text-000000, #e8e6e3) !important;
}
::selection {
    background-color: var(--darkreader-background-0060d4, #004daa) !important;
    color: var(--darkreader-text-ffffff, #e8e6e3) !important;
}
::-moz-selection {
    background-color: var(--darkreader-background-0060d4, #004daa) !important;
    color: var(--darkreader-text-ffffff, #e8e6e3) !important;
}
}</style><style class="darkreader darkreader--text" media="screen"></style><style class="darkreader darkreader--invert" media="screen">.jfk-bubble.gtx-bubble, .captcheck_answer_label > input + img, span#closed_text > img[src^="https://www.gstatic.com/images/branding/googlelogo"], span[data-href^="https://www.hcaptcha.com/"] > #icon, img.Wirisformula, a[data-testid="headerMediumLogo"]>svg, .d2l-navigation-link-image-container, .d2l-iframe-loading-container, div.mc-ip-hide[style*="background: rgb(255, 255, 255) !important"], [style*="color: rgb(0, 0, 1) !important;"], [src="https://github.githubassets.com/images/modules/site/icons/footer/github-logo.svg"], [src^="https://github.githubassets.com/images/modules/site/home/community-sponsor-"], [src^="https://github.githubassets.com/images/modules/site/home/community-readme-"], [src^="https://github.githubassets.com/images/modules/site/home/community-discussions-"], [src="https://github.githubassets.com/images/modules/site/home/dependabot-merge.png"], [src="https://github.githubassets.com/images/modules/site/home/dependabot-pr.png"], [src="https://github.githubassets.com/images/modules/site/home/gh-desktop.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-merge.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-comment.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-description.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-screen.png"], [src="https://github.githubassets.com/images/modules/site/home/enterprise-city-w-logos.jpg"], [src="https://github.githubassets.com/images/modules/site/codespaces/codespaces-icon.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/dependency-rust.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/dependency-3.png"], [src^="https://github.githubassets.com/images/modules/site/codespaces/dependencies-"], [src="https://github.githubassets.com/images/modules/site/codespaces/commit-3.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/extensions-1.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/extensions-2.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/commit-workflow.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/workflow-view.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/code.png"], [src="https://github.githubassets.com/images/email/explore/explore-gradient-icon.png"], [src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/collections/learn-to-code/learn-to-code.png"], .js-viewport-aware-video.color-bg-primary.width-full.d-block.codespaces-hero-video, .build-in-animate.position-relative.mb-6-fluid.box-shadow-active-mktg.mx-auto.home-mobile-iphone.build-in-slideY.js-build-in > .js-viewport-aware-video.width-full, .overflow-hidden.position-relative.box-shadow-active-border-mktg.rounded-2-fluid.color-bg-primary.build-in-scale-fade.js-build-in-item, .build-in-animate.overflow-hidden.box-shadow-active-border-mktg.rounded-2-fluid.position-relative.home-workflow-comp.js-build-in-item, .mx-lg-auto.col-lg-7.col-12, #hero-section-brand-heading {
    filter: invert(100%) hue-rotate(180deg) contrast(90%) !important;
}</style><style class="darkreader darkreader--inline" media="screen">[data-darkreader-inline-bgcolor] {
  background-color: var(--darkreader-inline-bgcolor) !important;
}
[data-darkreader-inline-bgimage] {
  background-image: var(--darkreader-inline-bgimage) !important;
}
[data-darkreader-inline-border] {
  border-color: var(--darkreader-inline-border) !important;
}
[data-darkreader-inline-border-bottom] {
  border-bottom-color: var(--darkreader-inline-border-bottom) !important;
}
[data-darkreader-inline-border-left] {
  border-left-color: var(--darkreader-inline-border-left) !important;
}
[data-darkreader-inline-border-right] {
  border-right-color: var(--darkreader-inline-border-right) !important;
}
[data-darkreader-inline-border-top] {
  border-top-color: var(--darkreader-inline-border-top) !important;
}
[data-darkreader-inline-boxshadow] {
  box-shadow: var(--darkreader-inline-boxshadow) !important;
}
[data-darkreader-inline-color] {
  color: var(--darkreader-inline-color) !important;
}
[data-darkreader-inline-fill] {
  fill: var(--darkreader-inline-fill) !important;
}
[data-darkreader-inline-stroke] {
  stroke: var(--darkreader-inline-stroke) !important;
}
[data-darkreader-inline-outline] {
  outline-color: var(--darkreader-inline-outline) !important;
}
[data-darkreader-inline-stopcolor] {
  stop-color: var(--darkreader-inline-stopcolor) !important;
}
[data-darkreader-inline-bg] {
  background: var(--darkreader-inline-bg) !important;
}
[data-darkreader-inline-border-short] {
  border: var(--darkreader-inline-border-short) !important;
}
[data-darkreader-inline-border-bottom-short] {
  border-bottom: var(--darkreader-inline-border-bottom-short) !important;
}
[data-darkreader-inline-border-left-short] {
  border-left: var(--darkreader-inline-border-left-short) !important;
}
[data-darkreader-inline-border-right-short] {
  border-right: var(--darkreader-inline-border-right-short) !important;
}
[data-darkreader-inline-border-top-short] {
  border-top: var(--darkreader-inline-border-top-short) !important;
}
[data-darkreader-inline-invert] {
    filter: invert(100%) hue-rotate(180deg);
}</style><style class="darkreader darkreader--variables" media="screen">:root {
   --darkreader-neutral-background: var(--darkreader-background-ffffff, #181a1b);
   --darkreader-neutral-text: var(--darkreader-text-000000, #e8e6e3);
   --darkreader-selection-background: var(--darkreader-background-0060d4, #004daa);
   --darkreader-selection-text: var(--darkreader-text-ffffff, #e8e6e3);
}</style><style class="darkreader darkreader--root-vars" media="screen"></style><meta name="darkreader" content="18589df980d74f839d66c32f96a3966d"><style class="darkreader darkreader--override" media="screen">.vimvixen-hint {
    background-color: var(--darkreader-background-ffd76e, #684b00) !important;
    border-color: var(--darkreader-background-c59d00, #9e7e00) !important;
    color: var(--darkreader-text-302505, #d7d4cf) !important;
}
#vimvixen-console-frame {
    color-scheme: light !important;
}
::placeholder {
    opacity: 0.5 !important;
}
#edge-translate-panel-body,
.MuiTypography-body1,
.nfe-quote-text {
    color: var(--darkreader-neutral-text) !important;
}
gr-main-header {
    background-color: var(--darkreader-background-add8e6, #1b4958) !important;
}
.tou-z65h9k,
.tou-mignzq,
.tou-1b6i2ox,
.tou-lnqlqk {
    background-color: var(--darkreader-neutral-background) !important;
}
.tou-75mvi {
    background-color: var(--darkreader-background-cfecf5, #0f3a47) !important;
}
.tou-ta9e87,
.tou-1w3fhi0,
.tou-1b8t2us,
.tou-py7lfi,
.tou-1lpmd9d,
.tou-1frrtv8,
.tou-17ezmgn {
    background-color: var(--darkreader-background-f5f5f5, #1e2021) !important;
}
.tou-uknfeu {
    background-color: var(--darkreader-background-faedda, #432c09) !important;
}
.tou-6i3zyv {
    background-color: var(--darkreader-background-85c3d8, #245d70) !important;
}
div.mermaid-viewer-control-panel .btn {
    background-color: var(--darkreader-neutral-background);
    fill: var(--darkreader-neutral-text);
}
svg g rect.er {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.entityBox {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.attributeBoxOdd {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.attributeBoxEven {
    fill: var(--darkreader-selection-background);
    fill-opacity: 0.8 !important;
}
svg rect.er.relationshipLabelBox {
    fill: var(--darkreader-neutral-background) !important;
}
svg g g.nodes rect,
svg g g.nodes polygon {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.task {
    fill: var(--darkreader-selection-background) !important;
}
svg line.messageLine0,
svg line.messageLine1 {
    stroke: var(--darkreader-neutral-text) !important;
}
div.mermaid .actor {
    fill: var(--darkreader-neutral-background) !important;
}
mitid-authenticators-code-app > .code-app-container {
    background-color: white !important;
    padding-top: 1rem;
}
iframe#unpaywall[src$="unpaywall.html"] {
    color-scheme: light !important;
}
select {
    --darkreader-bg--form-control-background-color: rgba(22, 22, 22, 0) !important;
}
body#tumblr {
    --darkreader-bg--secondary-accent: 31, 32, 34 !important;
    --darkreader-bg--white: 23, 23, 23 !important;
    --darkreader-text--black: 228, 224, 218 !important;
}
:host {
    --d2l-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-button-icon-background-color-hover: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-color-ferrite: var(--darkreader-neutral-text) !important;
    --d2l-color-sylvite: var(--darkreader-bg--d2l-color-sylvite) !important;
    --d2l-dropdown-background-color: var(--darkreader-neutral-background) !important;
    --d2l-dropdown-border-color: var(--darkreader-border--d2l-color-mica) !important;
    --d2l-input-backgroud-color: var(--darkreader-neutral-background) !important;
    --d2l-menu-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-tooltip-background-color: var(--darkreader-neutral-background) !important;
    --d2l-tooltip-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
:host([_floating]) .d2l-floating-buttons-container {
    background-color: var(--darkreader-neutral-background) !important;
    border-top-color: var(--darkreader-border--d2l-color-mica) !important;
    opacity: 0.88 !important;
}
d2l-card {
    background: var(--darkreader-neutral-background) !important;
    border-color: var(--darkreader-border--d2l-color-gypsum) !important;
}
d2l-dropdown-content > div,
d2l-menu-item {
    background-color: var(--darkreader-neutral-background) !important;
    border-radius: 10px !important;
}
d2l-empty-state-simple {
    border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-button-filter > ul > li > a.vui-button {
    border-color: var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-label-text:has(.d2l-button-subtle-content):hover,
.d2l-label-text:has(.d2l-button-subtle-content):focus,
.d2l-label-text:has(.d2l-button-subtle-content):active {
    background-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-navigation-centerer {
    color: inherit !important;
}
.d2l-tabs-layout {
    border-color: var(--darkreader-border--d2l-color-gypsum) !important;
}
.d2l-input,
.d2l-calendar-date,
.d2l-htmleditor-container {
    background-color: var(--darkreader-neutral-background) !important;
}
.d2l-collapsible-panel {
    border: 1px solid var(--darkreader-border--d2l-color-mica) !important;
    border-radius: 0.4rem !important;
}
.d2l-collapsible-panel-divider {
    border-bottom: 1px solid var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-w2d-flex {
    border-bottom: 2px solid var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-collapsible-panel scrolled,
.d2l-collapsible-panel-header,
.d2l-w2d-collection-fixed {
    background-color: var(--darkreader-neutral-background) !important;
}
.d2l-loading-spinner-bg {
    fill: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-loading-spinner-bg-stroke {
    stroke: var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-loading-spinner-wrapper svg path,
.d2l-loading-spinner-wrapper svg circle {
    fill: var(--darkreader-neutral-background) !important;
}
.d2l-twopanelselector-side.d2l-twopanelselector-side-sep {
    background: var(--darkreader-bg--d2l-color-mica) !important;
}
.d2l-le-TreeAccordionItem-anchor::before {
    background: var(--darkreader-bg--d2l-color-corundum) !important;
}
table[class|="moz-header"] {
    background: none;
}
*[style*="color: rgba(0,0,0,"],
*[style*="color: rgba(0, 0, 0,"],
*[style*="color:#000"],
*[style*="color:black"],
*[style*="color:#282828"],
*[style*="color:#444"] {
    color: var(--darkreader-neutral-text) !important;
}
*[style*="background:#fff"],
*[style*="background-color:#fff"] {
    background: var(--darkreader-neutral-background) !important;
}
*[bgcolor="#F5F5F5"],
*[style*="background-color: #F5F5F5"] {
    background: var(--darkreader-background-f5f5f5, #1e2021) !important;
}
body[style*="background: rgb(255, 255, 255) !important"] *:not(a),
.body[style*="background-color: rgb(254, 254, 254) !important"] *:not(a) {
    background-color: var(--darkreader-neutral-background) !important;
}
div[style*="www.gstatic.com/android/"] {
    background: none !important;
}
*[style*="background:#f9f9f9"] {
    background: var(--darkreader-background-f9f9f9, #1b1e1f) !important;
}
body.mediawiki.skin-vector #mw-page-base {
    background-image: none !important;
}
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
.blob-code-inner,
.blob-num,
.cm-s-github-light .CodeMirror-lines,
.CodeMirror pre > span,
.CodeMirror,
.CodeMirror-dialog input,
.CodeMirror-hints,
.CodeMirror-linenumber,
.CodeMirror-lines,
.commit .sha,
.commit .sha-block,
.commit-desc pre,
.commit-ref,
.commit-tease-sha,
.export-phrase pre,
.file-info,
.FormControl-input.FormControl-monospace,
.FormControl-select.FormControl-monospace,
.FormControl-textarea.FormControl-monospace,
.input-monospace,
.markdown-body .footnotes .data-footnote-backref g-emoji,
.pr-1 > code > a,
.react-blob-print-hide,
.react-code-text,
.react-code-view-edit .cm-s-github-light .CodeMirror-lines,
.text-mono *,
.text-mono,
.two-factor-recovery-codes,
[aria-labelledby*="codemirror"] *,
[class*="blob-code"] *,
code > a[class="Link--secondary"],
section[aria-labelledby*="file-name-id"] > div > div *,
span.commit-ref > a > *,
span.commit-ref > a {
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace !important;
}
.markdown-body code,
.markdown-title code {
    background-color: var(--darkreader-text-1b1f231a, rgba(212, 209, 203, 0.1)) !important;
}
.markdown-body pre code {
    background-color: transparent !important;
}
.refined-github .dashboard .js-all-activity-header + div {
    background-color: var(--darkreader-background-e4e5e9, #26292b) !important;
    border-color: var(--darkreader-background-bbc1c9, #3a3f42) !important;
}
.refined-github .dashboard-rollup-items .body {
    border-top-color: var(--darkreader-background-bbc1c9, #3a3f42) !important;
}
.refined-github .reaction-summary-item a {
    box-shadow: 0 0 0 2px var(--darkreader-background-ffffff, #181a1b) !important;
}
.refined-github button.reaction-summary-item {
    border-bottom: rgb(77, 172, 253) !important;
    border-top-color: rgb(52, 59, 68) !important;
}
.js-site-search-form {
    background-color: #ffffff1a !important;
    border-radius: 2pt !important;
}
.blob-num:not(.cc-coverage-covered-border):not(.cc-coverage-missed-border) {
    border-right: 0 !important;
}
.cc-issue-description {
    color: #24292e !important;
}
.cc-readup-background {
    background-color: rgb(28, 30, 31) !important;
}
.cc-readup-content {
    border-left: 1px solid grey !important;
    color: rgb(216, 214, 208) !important;
}
.cc-readup-content blockquote {
    border-left: 3px solid dimgrey !important;
}
.cc-pr__link-text {
    color: darkgrey !important;
}
.cc-pr__tooltip {
    background-color: rgb(28, 30, 31) !important;
    color: darkgrey !important;
}
.jfk-bubble,
.octotree-sidebar,
.cc-pr__logo,
.cc-octicon,
#network canvas,
img.network-tree {
    filter: invert(94.4%) hue-rotate(180deg) contrast(90%) !important;
}
#commit-activity-detail > svg {
    fill: var(--darkreader-text-000000, #e8e6e3) !important;
}
.ContributionCalendar-day,
.ContributionCalendar-day[data-level="0"] {
    fill: var(--color-calendar-graph-day-bg) !important;
}
.ContributionCalendar-day[data-level="1"] {
    fill: var(--color-calendar-graph-day-L1-bg) !important;
}
.ContributionCalendar-day[data-level="2"] {
    fill: var(--color-calendar-graph-day-L2-bg) !important;
}
.ContributionCalendar-day[data-level="3"] {
    fill: var(--color-calendar-graph-day-L3-bg) !important;
}
.ContributionCalendar-day[data-level="4"] {
    fill: var(--color-calendar-graph-day-L4-bg) !important;
}
.day,
.day[data-Count="0"] {
    fill: var(--color-calendar-graph-day-bg) !important;
}
.day[data-Count="1"] {
    fill: var(--color-calendar-graph-day-L1-bg) !important;
}
.day[data-Count="2"] {
    fill: var(--color-calendar-graph-day-L2-bg) !important;
}
.day[data-Count="3"] {
    fill: var(--color-calendar-graph-day-L3-bg) !important;
}
.day[data-Count="4"] {
    fill: var(--color-calendar-graph-day-L4-bg) !important;
}
:root {
    --color-calendar-graph-day-bg: var(--darkreader-background-ebedf0, #222526) !important;
    --color-calendar-graph-day-L1-bg: var(--darkreader-background-9be9a8, #166634) !important;
    --color-calendar-graph-day-L2-bg: var(--darkreader-background-40c463, #2f9a5f) !important;
    --color-calendar-graph-day-L3-bg: var(--darkreader-background-30a14e, #26813e) !important;
    --color-calendar-graph-day-L4-bg: var(--darkreader-text-216e39, #8bdca4) !important;
    --color-previewable-comment-form-bg: var(--darkreader-neutral-background) !important;
}
.Box-row--yellow {
    background-color: var(--darkreader-background-fffbdd, #362f00) !important;
}
.merge-status-list {
    border-color: var(--darkreader-background-c0c5c7, #3a3e41) !important;
}
.user-has-reacted {
    background-color: rgba(17, 88, 199, 0.2) !important;
}
.hx_IssueLabel,
span[class*="TokenBase"] {
    background: rgba(var(--label-r),var(--label-g),var(--label-b),var(--background-alpha)) !important;
    border-color: hsla(var(--label-h),calc(var(--label-s) * 1%),calc((var(--label-l) + var(--lighten-by)) * 1%),var(--border-alpha)) !important;
    color: hsl(var(--label-h),calc(var(--label-s) * 1%),calc((var(--label-l) + var(--lighten-by)) * 1%)) !important;
}
.header-search-input {
    border: 0 !important;
}
.HeaderMenu-link--sign-in {
    border: 0 !important;
}
.timeline-comment--caret.current-user::after {
    --color-current-user-tip-bg: var(--darkreader-bg--color-box-bg-info) !important;
}
.timeline-comment--caret.current-user::before {
    background-color: var(--darkreader-border--color-box-border-info) !important;
}
@media screen and (min-width: 1012px) {
    markdown-toolbar.border-lg-top-0 {
        border-top: 1px solid var(--darkreader-border--color-border-primary) !important;
    }
}
@media screen and (max-width: 767px) {
    div.tabnav--responsive button.tabnav-tab {
        --color-border-primary: var(--darkreader-border--color-border-primary) !important;
    }
}
.TimelineItem-badge[style^="background-color: var(--color-timeline-merged-bg)"] {
    background-color: var(--color-timeline-merged-bg) !important;
}
.ContributionCalendar-label {
    --color-text-primary: var(--darkreader-neutral-text) !important;
}
article div[style^="background: linear-gradient"] {
    background: linear-gradient(to top, var(--darkreader-bg--color-bg-primary), transparent) !important;
}
.ͼ5 .cm-content,
.ͼ5 .cm-panel.cm-search > button {
    background-color: var(--darkreader-neutral-background) !important;
}</style><style>
:root {
  --fontStack-monospace: "Monaspace Neon", ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace !important;
}
</style><style class="darkreader darkreader--sync" media="screen"></style>




  
    
  <link rel="dns-prefetch" href="https://github.githubassets.com/">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com/">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com/" crossorigin="">
  <link rel="preconnect" href="https://avatars.githubusercontent.com/">

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/light-2ff56e1b36116ee2.css"><style class="darkreader darkreader--sync" media="screen"></style><link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/dark-2d1fe43dbc9adf1f.css"><style class="darkreader darkreader--sync" media="screen"></style><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-f7f95d7633592089.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-e4bbc49fc7b82570.css"><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast-cc3f126b45166b83.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-652ca611ea4e33fe.css"><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast-9e82d635cb6c3f49.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-d530ee188d165539.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-3ad0ec21150df75b.css"><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast-5691ff467f71a3f6.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-abee7710893cd168.css"><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast-eafcf6cd46158360.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-c7974682a1a84c8d.css"><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast-f8dab3e04f94c501.css">

  <style type="text/css">
    :root {
      --tab-size-preference: 4;
    }

    pre, code {
      tab-size: var(--tab-size-preference);
    }
  </style><style class="darkreader darkreader--sync" media="screen"></style>

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/primer-primitives-7f694b60439d06c0.css"><style class="darkreader darkreader--sync" media="screen"></style>
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/primer-tailwind-compatible-25aee10cf9257254.css"><style class="darkreader darkreader--sync" media="screen"></style>
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/global-b40ec823a1a6a1af.css"><style class="darkreader darkreader--sync" media="screen"></style>
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/github-f825c0edd7ad57f8.css"><style class="darkreader darkreader--sync" media="screen"></style>
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/tailwind-00bf83f0a2a87752.css"><style class="darkreader darkreader--sync" media="screen"></style>
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/repository-0751f482f5210958.css"><style class="darkreader darkreader--sync" media="screen"></style>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/code-c22301b4e838281c.css"><style class="darkreader darkreader--sync" media="screen"></style>

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["actions_custom_images_storage_billing_ui_visibility","actions_image_version_event","actions_workflow_language_service_allow_case_function","actions_workflow_language_service_allow_concurrency_queue","agent_conflict_resolution","alternate_user_config_repo","arianotify_comprehensive_migration","billing_discount_threshold_notification","billing_ui_budget_pagination_enabled","code_scanning_dfa_degraded_experience_notice","code_view_checks_live_updates","codemirror_inp_optimizations","codeowners_validation_in_diff","codespaces_prebuild_region_target_update","codespaces_tab_react","coding_agent_model_selection","coding_agent_model_selection_all_skus","comment_viewer_copy_raw_markdown","contentful_primer_code_blocks","copilot_agent_snippy","copilot_api_agentic_issue_marshal_yaml","copilot_ask_mode_dropdown","copilot_automation_session_author","copilot_capi_error_response_telemetry","copilot_chat_alternative_global_nav_actions","copilot_chat_attach_multiple_images","copilot_chat_category_rate_limit_messages","copilot_chat_clear_model_selection_for_default_change","copilot_chat_contextual_suggestions_updated","copilot_chat_disable_model_picker_while_streaming","copilot_chat_enable_tool_call_logs","copilot_chat_file_redirect","copilot_chat_increase_token_padding","copilot_chat_input_commands","copilot_chat_opening_thread_switch","copilot_chat_prettify_pasted_code","copilot_chat_reduce_quota_checks","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_preview_gate","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_diff_explain_conversation_intent","copilot_diff_reference_context","copilot_disable_cfi_sku_new_signups","copilot_duplicate_thread","copilot_extensions_hide_in_dotcom_chat","copilot_extensions_removal_on_marketplace","copilot_features_sql_server_logo","copilot_file_block_ref_matching","copilot_ftp_hyperspace_upgrade_prompt","copilot_icebreakers_experiment_dashboard","copilot_icebreakers_experiment_hyperspace","copilot_immersive_code_block_transition_wrap","copilot_immersive_embedded","copilot_immersive_embedded_deferred_payload","copilot_immersive_embedded_draggable","copilot_immersive_embedded_header_button","copilot_immersive_embedded_implicit_references","copilot_immersive_file_block_transition_open","copilot_immersive_file_preview_keep_mounted","copilot_immersive_job_result_preview","copilot_immersive_structured_model_picker","copilot_immersive_task_hyperlinking","copilot_immersive_task_within_chat_thread","copilot_issue_list_show_more","copilot_mc_cli_resume_any_users_task","copilot_mission_control_always_send_integration_id","copilot_mission_control_cli_session_status","copilot_mission_control_initial_data_spinner","copilot_mission_control_logs_incremental","copilot_mission_control_task_alive_updates","copilot_org_policy_page_focus_mode","copilot_premium_request_quotas","copilot_redirect_header_button_to_agents","copilot_resource_panel","copilot_scroll_preview_tabs","copilot_share_active_subthread","copilot_spaces_ga","copilot_spaces_individual_policies_ga","copilot_spaces_pagination","copilot_spark_empty_state","copilot_spark_handle_nil_friendly_name","copilot_swe_agent_hide_model_picker_if_only_auto","copilot_swe_agent_pr_comment_model_picker","copilot_swe_agent_use_subagents","copilot_task_api_github_rest_style","copilot_unconfigured_is_inherited","copilot_upgrade_freeze","copilot_usage_metrics_ga","copilot_workbench_slim_line_top_tabs","custom_instructions_file_references","dashboard_indexeddb_caching","dashboard_lists_max_age_filter","dashboard_universe_2025","dashboard_universe_2025_feedback_dialog","dead_click_detection","dotgithub_fork_warning","fgpat_permissions_selector_redesign","flex_cta_groups_mvp","github_models_scheduled_hydro_events","global_nav_react","hide_groups_list_for_few_groups","hyperspace_2025_logged_out_batch_1","hyperspace_2025_logged_out_batch_2","hyperspace_2025_logged_out_batch_3","ipm_global_transactional_message_agents","ipm_global_transactional_message_copilot","ipm_global_transactional_message_issues","ipm_global_transactional_message_prs","ipm_global_transactional_message_repos","ipm_global_transactional_message_spaces","issue_cca_modal_open","issue_cca_multi_assign_modal","issue_cca_task_side_panel","issue_cca_visualization","issue_cca_visualization_session_panel","issue_fields_global_search","issues_expanded_file_types","issues_lazy_load_comment_box_suggestions","issues_react_bots_timeline_pagination","issues_react_chrome_container_query_fix","issues_react_include_bots_in_pickers","issues_react_ui_feedback","issues_search_type_gql","landing_pages_ninetailed","landing_pages_web_vitals_tracking","lifecycle_label_name_updates","low_quality_classifier","marketing_pages_search_explore_provider","memex_default_issue_create_repository","memex_live_update_hovercard","memex_mwl_filter_field_delimiter","memex_remove_deprecated_type_issue","memex_roadmap_drag_style","merge_status_header_feedback","notifications_menu_defer_labels","oauth_authorize_clickjacking_protection","octocaptcha_origin_optimization","pr_sfv_new_diff_fetch","prs_checks_react","prs_conversations_react","prs_css_anchor_positioning","prs_live_updates_issue_comments","prs_load_all_alerts","prx_files","pull_request_commit_checks_dialog","pull_request_files_accurate_size_estimates","pull_request_files_virtualization","pull_request_inbox_new_sections","pull_request_merge_status_button","pull_request_virtualization_preload_diffs","pulls_new_es_degraded_banner","react_blob_overlay","repository_suggester_elastic_search","rules_insights_filter_bar_created","sample_network_conn_type","secret_scanning_pattern_alerts_link","security_center_artifact_filters_popover","session_logs_ungroup_reasoning_text","site_features_copilot_universe","site_homepage_collaborate_video","spark_prompt_secret_scanning","spark_server_connection_status","suppress_automated_browser_vitals","team_review_requested_by_user_filter","ui_skip_on_anchor_click","viewscreen_sandbox","warn_inaccessible_attachments","webp_support","workbench_store_readonly"],"login":"KonstaNtinAleKseeVicHtheonly","copilotApiOverrideUrl":"https://api.individual.githubcopilot.com"}</script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/wp-runtime-d7310dc770a7ac2d.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/fetch-utilities-3140609b5732710f.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/28839-7adfdde5afeb1a03.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/85924-ac5602ef611dc506.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/34646-4c7883eb242d5210.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/environment-a12df3cf35884818.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/runtime-helpers-cb4dfbc9d23f30be.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/2966-d68f2b4558d86113.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/96232-540ff5f81016a9ca.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/41013-647932573fc130af.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/51210-45dfb7dd106f6b96.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/64247-73a9861fe185671f.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/81683-382ccc88e034ea1d.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/9338-f6bee5a8d66d930f.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/46740-5a373320e5ef9c01.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/67466-79abcbf599986a00.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/github-elements-61af8f0198be4afd.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/element-registry-161b4fbd68395409.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/react-core-1bf2dfbca21efd20.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/react-lib-1353f2cef82bcdc0.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/58889-5b136bc717e57a8b.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/79039-69acf717ffc901a4.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/61110-073153e0413daf3a.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/2887-91b9c645d570616a.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/26533-f22c29ae5e9b1ed2.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/86483-c3a819d46503a3da.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/37460-fcd4830a1194eace.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/60481-24b13ea726837f7b.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/46287-853bfcb69bb5b3f9.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/2498-f0375ed070e22e54.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/61025-5b1312da907b4074.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/89627-40275597692dc855.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/79087-4f706db8aa2ec0fb.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/49029-42bd0899fca05960.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/99328-a2c6b180d25cb160.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/behaviors-05170beef7088f93.js.Без названия" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/react-core.f25ad6e4b6a65cba.module.css"><style class="darkreader darkreader--sync" media="screen"></style>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/4244-97fb660009234136.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/notifications-global-442a23b66c306470.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/39373-075d662e5ab13538.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/code-menu-ad3e18f5935a3ed8.js.Без названия" defer="defer"></script>
  
  <script crossorigin="anonymous" type="module" src="./project_tests_postman_files/primer-react-ed05dc3d91bca0bd.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/octicons-react-60e727d7a1b6f52c.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/89960-3369b8943362e07e.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/37869-3811d0fa923a406d.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/68751-830b37204cdf7847.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/7463-30e02617b93e1c07.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/15272-0fca7ba11b03440f.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/32769-abc9916acf2cd4f1.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/36505-9798da05fe2143ec.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/46148-264173ef30e2e838.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/57712-c58bee9c0d90a66f.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/61545-6a3a31f92bb5e61a.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/20999-9b5648501d55c42d.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/98228-7a59d90d972526cc.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/63991-466700d8cea41498.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/59852-fc77b3df0a08d405.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/3624-fdb7d4ead672734b.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/66231-9febf100ccdfe155.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/71001-7431ccad12c501aa.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/33684-bbaee6839ab84dd8.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/18222-8b85d637a2041072.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/96755-770967b1236437cd.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/4916-0bb8c44ba1b3d0f7.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/75674-28ffd7157e7cb9e8.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/75601-d9eafa1fbbb5172b.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/8987-366fbcea269300af.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/38184-1e8a3a630d385487.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/41110-df3d2329c8277a27.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/22216-7b6bcf152c4599f6.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/32639-b4f0cdce4bef4ac5.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/58085-77d3143b51231967.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/66519-27db8d6ec9c71a98.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/50110-0f4d902364ca3e5b.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/26497-bb0dd27f414e3e71.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/49135-5f8ca97edb189a81.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/71920-723318c28b0f8f3a.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./project_tests_postman_files/code-view-121a46f29c0d4946.js.Без названия" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/primer-react-css.00ba154d21e54e53.module.css"><style class="darkreader darkreader--sync" media="screen"></style>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/code-view.63b52bc3543633b9.module.css"><style class="darkreader darkreader--sync" media="screen"></style>


  <title>fastapi-shop/backend/test_commands.md at master · s6ptember/fastapi-shop</title>



  <meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)" data-turbo-transient="">
  <meta name="route-controller" content="blob" data-turbo-transient="">
  <meta name="route-action" content="show" data-turbo-transient="">
  <meta name="fetch-nonce" content="v2:a8bf5113-53e5-eb8b-0c44-e454e8a6de97">

    
  <meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb">


  <meta name="request-id" content="24CC:37BA98:4FDB54A:3E138F5:69F22C26" data-turbo-transient="true"><meta name="html-safe-nonce" content="d9083b18268618a7a93934bd98f14a9674515326e658287532b9daa1c2e2b9f2" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9zNnB0ZW1iZXIvZmFzdGFwaS1zaG9wL3RyZWUvbWFzdGVyL2Zyb250ZW5kIiwicmVxdWVzdF9pZCI6IjI0Q0M6MzdCQTk4OjRGREI1NEE6M0UxMzhGNTo2OUYyMkMyNiIsInZpc2l0b3JfaWQiOiIzODI1NjI5NTMyNDAxMTQ1NzE4IiwicmVnaW9uX2VkZ2UiOiJmcmEiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-turbo-transient="true"><meta name="visitor-hmac" content="4effad85ff1b218f1c457067901f16852323251c8d35e340e88c9d8374675d04" data-turbo-transient="true">


    <meta name="hovercard-subject-tag" content="repository:1075982471" data-turbo-transient="">


  <meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true">
  

  <meta name="selected-link" value="repo_source" data-turbo-transient="">
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="163430420"><meta name="octolytics-actor-login" content="KonstaNtinAleKseeVicHtheonly"><meta name="octolytics-actor-hash" content="3ede1b1324138bfffce919a5110eb9f1c981daf94fddf837ad539cdbd64afd71">





  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true">

  




    <meta name="user-login" content="KonstaNtinAleKseeVicHtheonly">

  <link rel="sudo-modal" href="https://github.com/sessions/sudo_modal">

    <meta name="viewport" content="width=device-width">

    

      <meta name="description" content="Contribute to s6ptember/fastapi-shop development by creating an account on GitHub.">

      <link rel="search" type="application/opensearchdescription+xml" href="https://github.com/opensearch.xml" title="GitHub">

    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/s6ptember/fastapi-shop/blob/master/backend/app/schemas/cart.py">

      <meta name="twitter:image" content="https://opengraph.githubassets.com/273432a29a4cbfea2529ad7ad1e863c818647380aac2d55070052dd9ab894d99/s6ptember/fastapi-shop"><meta name="twitter:site" content="@github"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="fastapi-shop/backend/app/schemas/cart.py at master · s6ptember/fastapi-shop"><meta name="twitter:description" content="Contribute to s6ptember/fastapi-shop development by creating an account on GitHub.">
  <meta property="og:image" content="https://opengraph.githubassets.com/273432a29a4cbfea2529ad7ad1e863c818647380aac2d55070052dd9ab894d99/s6ptember/fastapi-shop"><meta property="og:image:alt" content="Contribute to s6ptember/fastapi-shop development by creating an account on GitHub."><meta property="og:image:width" content="1200"><meta property="og:image:height" content="600"><meta property="og:site_name" content="GitHub"><meta property="og:type" content="object"><meta property="og:title" content="fastapi-shop/backend/app/schemas/cart.py at master · s6ptember/fastapi-shop"><meta property="og:url" content="https://github.com/s6ptember/fastapi-shop/blob/master/backend/app/schemas/cart.py"><meta property="og:description" content="Contribute to s6ptember/fastapi-shop development by creating an account on GitHub.">
  


      <link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/163430420/ws?session=eyJ2IjoiVjMiLCJ1IjoxNjM0MzA0MjAsInMiOjIwMTc2MjY4MTgsImMiOjE2MzU0NzY2NTUsInQiOjE3Nzc0Nzg3MDR9--dd34488a3a956bcd8eaedbc309bf558ff2f8bc4c608b5afd27e85fd2cfce8948" data-refresh-url="/_alive" data-session-id="7160513f25a9c98e5ce12245f8e75ce0df2ca3af297ca28a1a02721743037b52">
      <link rel="shared-web-socket-src" href="https://github.com/assets-cdn/worker/socket-worker-4b32331dd8a8013e.js">

      <link rel="service-worker-src" href="https://github.com/assets-cdn/worker/service-worker-5aade1ce2fbab0fc.js?current_user=KonstaNtinAleKseeVicHtheonly&amp;errors_url=https%3A%2F%2Fapi.github.com%2F_private%2Fbrowser%2Ferrors&amp;release=aa7e481e529b8bf86e4ab4c175dd8ba8b590f9e9&amp;actor_id=163430420&amp;is_staff=false&amp;analytics_collector_url=https%3A%2F%2Fcollector.github.com%2Fgithub%2Fcollect">

      <meta name="hostname" content="github.com">


      <meta name="keyboard-shortcuts-preference" content="all">
      <meta name="hovercards-preference" content="true">
      <meta name="announcement-preference-hovercard" content="true">

        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="d7f61b46e9f3584a69e68e90407407147bb81e66d129e466b37a2596ec1733b5" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="568c098497d98702bac1642a2a853732a047a6ced28eabd3e15d50041a890235" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="87721d1504a187fb3fcbfa6e98526d058edf6fa1163680dbb36bf70525df6ac4" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="d19c7384fc11f41c248a1f6fd323e0667dd556e14bc2dea777f4817668066de7" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient="">

    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/s6ptember/fastapi-shop git https://github.com/s6ptember/fastapi-shop.git">

  <meta name="octolytics-dimension-user_id" content="190271353"><meta name="octolytics-dimension-user_login" content="s6ptember"><meta name="octolytics-dimension-repository_id" content="1075982471"><meta name="octolytics-dimension-repository_nwo" content="s6ptember/fastapi-shop"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="1075982471"><meta name="octolytics-dimension-repository_network_root_nwo" content="s6ptember/fastapi-shop">
  



    

    <meta name="turbo-body-classes" content="logged-in env-production page-responsive">
  <meta name="disable-turbo" content="false">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="release" content="aa7e481e529b8bf86e4ab4c175dd8ba8b590f9e9">
  <meta name="ui-target" content="full">

  <link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon-dark.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon-dark.svg" data-base-href="https://github.githubassets.com/favicons/favicon">

<meta name="theme-color" content="#181c1f">
<meta name="color-scheme" content="light dark">


  <link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials">

  <link rel="stylesheet" type="text/css" href="./project_tests_postman_files/81758.4296a1c7ae7b0023.module.css" crossorigin="anonymous"><style class="darkreader darkreader--sync" media="screen"></style><link rel="stylesheet" type="text/css" href="./project_tests_postman_files/38963.cb21c1afb12a325d.module.css" crossorigin="anonymous"><style class="darkreader darkreader--sync" media="screen"></style><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style class="darkreader darkreader--sync" media="screen"></style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><style class="darkreader darkreader--sync" media="screen"></style><link rel="stylesheet" type="text/css" href="./project_tests_postman_files/41922.116b96e3c7de1450.module.css" crossorigin="anonymous"><style class="darkreader darkreader--sync" media="screen"></style><link rel="stylesheet" type="text/css" href="./project_tests_postman_files/53839.518e4824386ed12c.module.css" crossorigin="anonymous"><style class="darkreader darkreader--sync" media="screen"></style><link rel="stylesheet" type="text/css" href="./project_tests_postman_files/37103.0defbbf240b7b8d8.module.css" crossorigin="anonymous"><style class="darkreader darkreader--sync" media="screen"></style><link rel="stylesheet" type="text/css" href="./project_tests_postman_files/26107.7c90bbab0c8d55f5.module.css" crossorigin="anonymous"><style class="darkreader darkreader--sync" media="screen"></style></head>

  <body class="logged-in env-production page-responsive" style="word-wrap: break-word;">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      <div id="__primerPortalRoot__" role="region" style="z-index: 1000; position: absolute; width: 100%;" data-turbo-permanent=""></div>
      

    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#start-of-content" data-skip-target-assigned="false" class="tmp-p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/primer-react-css.00ba154d21e54e53.module.css"><style class="darkreader darkreader--sync" media="screen"></style>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/keyboard-shortcuts-dialog.1ac5611d6700bff4.module.css"><style class="darkreader darkreader--sync" media="screen"></style>

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA__r_3n___">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>





      

          

                  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/primer-react-css.00ba154d21e54e53.module.css"><style class="darkreader darkreader--sync" media="screen"></style>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./project_tests_postman_files/global-nav-bar.8da6b9c71bfd4f74.module.css"><style class="darkreader darkreader--sync" media="screen"></style>

<react-partial partial-name="global-nav-bar" data-ssr="true" data-attempted-ssr="true" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"contextRegion":{"crumbs":[{"crumb_type":"user","label":"s6ptember","is_root":false,"href":"/s6ptember"},{"crumb_type":"repository","label":"fastapi-shop","is_root":false,"href":"/s6ptember/fastapi-shop"}],"localNavigation":[{"id":"code","icon":"code","label":"Code","href":"/s6ptember/fastapi-shop","selectedLinks":["repo_source","repo_downloads","repo_commits","repo_releases","repo_tags","repo_branches","repo_packages","repo_deployments","repo_attestations"],"popoverTarget":false,"commandId":"repositories:go-to-code","reactNav":{"appTarget":"code-view","anchor":"code-view-repo-link"},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"issues","icon":"issue-opened","label":"Issues","href":"/s6ptember/fastapi-shop/issues","selectedLinks":["repo_issues","repo_labels","repo_milestones"],"count":1,"popoverTarget":false,"commandId":"repositories:go-to-issues","reactNav":{"appTarget":"issues-react","anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"pull-requests","icon":"git-pull-request","label":"Pull requests","href":"/s6ptember/fastapi-shop/pulls","selectedLinks":["repo_pulls","checks"],"count":0,"popoverTarget":false,"commandId":"repositories:go-to-pull-requests","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"actions","icon":"play","label":"Actions","href":"/s6ptember/fastapi-shop/actions","selectedLinks":["repo_actions"],"popoverTarget":false,"commandId":"repositories:go-to-actions","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"projects","icon":"table","label":"Projects","href":"/s6ptember/fastapi-shop/projects","selectedLinks":["repo_projects","new_repo_project","repo_project"],"popoverTarget":false,"commandId":"repositories:go-to-projects","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"security-and-quality","icon":"shield","label":"Security and quality","href":"/s6ptember/fastapi-shop/security","selectedLinks":["security","overview","alerts","policy","token_scanning","code_scanning"],"count":0,"popoverTarget":false,"commandId":"repositories:go-to-security","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"insights","icon":"graph","label":"Insights","href":"/s6ptember/fastapi-shop/pulse","selectedLinks":["repo_graphs","repo_contributors","dependency_graph","dependabot_updates","pulse","people","community"],"popoverTarget":false,"commandId":"repositories:go-to-insights","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}}],"localNavigationUpdateChannel":"eyJjIjoicmVwbzoxMDc1OTgyNDcxOnVzZXI6MTYzNDMwNDIwOnNldHRpbmdzIiwidCI6MTc3NzQ3ODcwM30=--27b25132cf322b94269a9709ca3d2a34fbbddce668a94624d1a3603a15098784","selectedLink":null,"currentPath":"/s6ptember/fastapi-shop/blob/master/backend/app/schemas/cart.py"},"userMenu":{"owner":{"login":"KonstaNtinAleKseeVicHtheonly","name":null,"avatarUrl":"https://avatars.githubusercontent.com/u/163430420?v=4"}},"headerLogo":{"href":"/","aria-label":"Homepage "},"notifications":{"indicatorMode":"none","websocketChannel":"eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTYzNDMwNDIwIiwidCI6MTc3NzQ3ODcwM30=--c84356efaf9cf7d762cee2555c3c8dba8d2df2dd92c97f1007c28836846d9f93","fetchIndicatorSrc":"/notifications/indicator","fetchIndicatorEnabled":true},"issues":{"href":"/issues"},"pulls":{"href":"/pulls"},"contributedRepos":{"show":true,"href":"/repos"},"copilot":{"show":false,"showAgentsButton":false,"copilotChatUrl":null,"copilotApiUrl":"https://api.individual.githubcopilot.com"},"search":{"show":true,"showCommandPalette":false,"isSearchPage":false,"isJumpToSearch":false,"searchContext":{"scope":"repo:s6ptember/fastapi-shop","current_repo_name":"fastapi-shop","current_repo_nwo":"s6ptember/fastapi-shop","user_id":"s6ptember"}},"enterpriseBanner":{"show":false},"globalTransactionalMessage":null,"payloadsUrl":"/_global-navigation/payloads.json?current_repo_nwo=s6ptember%2Ffastapi-shop\u0026repository=fastapi-shop\u0026return_to=https%3A%2F%2Fgithub.com%2Fs6ptember%2Ffastapi-shop%2Fblob%2Fmaster%2Fbackend%2Fapp%2Fschemas%2Fcart.py\u0026user_id=s6ptember"}}</script>
  <div data-target="react-partial.reactRoot"><link rel="preload" as="image" href="./project_tests_postman_files/163430420"><header role="banner" aria-label="Global Navigation Menu" class="GlobalNav styles-module__appHeader__YzYWk prc-Stack-Stack-UQ9k6" data-gap="none" data-direction="vertical" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="none"><div class="prc-Stack-Stack-UQ9k6" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="center" data-padding="none"><div data-testid="top-nav-left" class="styles-module__left__Fylw7 styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="normal"><div data-loading-wrapper="true"><button data-component="IconButton" type="button" aria-haspopup="dialog" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_apb_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-three-bars" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path></svg></button></div><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" aria-hidden="true" id="_R_apb_" popover="auto">Open menu</span><div class="d-none"></div><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderHome__nkA_U prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_cpb_" href="https://github.com/" data-discover="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-mark-github" viewBox="0 0 24 24" width="32" height="32" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.226 17.284c-2.965-.36-5.054-2.493-5.054-5.256 0-1.123.404-2.336 1.078-3.144-.292-.741-.247-2.314.09-2.965.898-.112 2.111.36 2.83 1.01.853-.269 1.752-.404 2.853-.404 1.1 0 1.999.135 2.807.382.696-.629 1.932-1.1 2.83-.988.315.606.36 2.179.067 2.942.72.854 1.101 2 1.101 3.167 0 2.763-2.089 4.852-5.098 5.234.763.494 1.28 1.572 1.28 2.807v2.336c0 .674.561 1.056 1.235.786 4.066-1.55 7.255-5.615 7.255-10.646C23.5 6.188 18.334 1 11.978 1 5.62 1 .5 6.188.5 12.545c0 4.986 3.167 9.12 7.435 10.669.606.225 1.19-.18 1.19-.786V20.63a2.9 2.9 0 0 1-1.078.224c-1.483 0-2.359-.808-2.987-2.313-.247-.607-.517-.966-1.034-1.033-.27-.023-.359-.135-.359-.27 0-.27.45-.471.898-.471.652 0 1.213.404 1.797 1.235.45.651.921.943 1.483.943.561 0 .92-.202 1.437-.719.382-.381.674-.718.944-.943"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" aria-hidden="true" popover="auto"><span id="_R_cpb_">Homepage <span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->g then d<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true" data-component="Tooltip.KeybindingHintContainer"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">d</span><span aria-hidden="true">D</span></span></kbd></span></span><div class="d-none"></div></div><div data-testid="top-nav-center" class="styles-module__center__R3QRv styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="normal"><nav class="styles-module__contextRegion__VbSp2 prc-Breadcrumbs-BreadcrumbsBase-3Gb-B" aria-label="Breadcrumbs" data-overflow="menu" data-variant="normal"><ol class="prc-Breadcrumbs-BreadcrumbsList-BKjpe"><li class="prc-Breadcrumbs-ItemWrapper-k0NLn"><a class="styles-module__contextCrumb__IzGIq prc-Breadcrumbs-Item-jcraJ" href="https://github.com/s6ptember" data-discover="true"><span class="">s6ptember</span></a></li><li class="prc-Breadcrumbs-ItemWrapper-k0NLn"><a class="styles-module__contextCrumb__IzGIq prc-Breadcrumbs-Item-jcraJ" href="https://github.com/s6ptember/fastapi-shop" data-discover="true"><span class="styles-module__contextCrumbLast__tI2e3">fastapi-shop</span></a></li></ol></nav><div class="Search-module__searchButtonGroup__aetw5 prc-ButtonGroup-ButtonGroup-vFUrY"><div><button data-component="Button" type="button" aria-label="Search or jump to…" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ Search-module__searchButton__aiE0a" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="Search-module__placeholder__p9hbG Search-module__text__veSYi Search-module__value__TFoak">Type <kbd class="Search-module__kbd__WCskr">/</kbd> to search</span></span></span></button></div><div></div></div><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ Search-module__smallSearchButton___8Gvn prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_2l9b_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" aria-hidden="true" popover="auto"><span id="_R_2l9b_">Search or jump to…<span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->forward slash<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true" data-component="Tooltip.KeybindingHintContainer"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">forward slash</span><span aria-hidden="true">/</span></span></kbd></span></span><div class="d-none"></div><div class="d-none"><qbsearch-input class="search-input" data-scope="repo:s6ptember/fastapi-shop" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="DTvlJAEYdJ6l0lC6nOr2sOeWtMFdVpQm0-8NPq9hbgmU6mcUFZIeMsUYprD3fUhV4GvHi0xQMo7cLh3ssahJOg" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="s6ptember/fastapi-shop" data-current-org="" data-current-owner="s6ptember" data-logged-in="true" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">

    <input type="hidden" name="type" class="js-site-search-type-field" wfd-id="id63">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-3aae17c0-55da-4248-815b-8e7ae9d8580a" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" wfd-id="id64">
          </div>
        </div>
          <span data-target="query-builder.clearButton" hidden="">
            <span class="sr-only" id="query-builder-test-clear">Clear</span>
            <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-action="
                  click:query-builder#clear
                  focus:query-builder#clearButtonFocus
                  blur:query-builder#clearButtonBlur
                " variant="small" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 tmp-mr-1 px-2 tmp-px-2 py-0 tmp-py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

          </span>
      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                        <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                combobox-commit:query-builder#comboboxCommit
                mousedown:query-builder#resultsMousedown
              " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results" tabindex="-1"></ul>

        </div>
      <div class="FormControl-inlineValidation" id="validation-3aae17c0-55da-4248-815b-8e7ae9d8580a" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted tmp-px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2 tmp-ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2 tmp-ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="utw02nTYashzM42PW_pRH2p3djcNV1lFwKDa9djUfThpRIvSp1f0xqHexCESCp5PoObgBvivAYdss4WldOFewA" wfd-id="id65">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox" wfd-id="id66">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="GzFLobsC3nMfl99kVUqgTfZaJU9XJY2genqS4bwEW3JppHlhSuRDZkFU6CF6vzagz49TJ78eXP9rT4mpglaQNg" wfd-id="id67">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField" wfd-id="id68">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false" wfd-id="id69">
              <input type="hidden" value="rOZ7OPZsmd3xlqhTG90YWU5VcHo_j1c2HJ5xhXOiLM2rGYCwtc5PC9PISf0D33QX0vy9OL4_N9JNhZZEZyvyDw" data-csrf="true" wfd-id="id70">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500" wfd-id="id71">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="bxaZrebgw6dEtVHK86L0kqnbMIYn8_DcpT-jv0r_jmkHVKDTR8MKYyC48N7M9OzBYtJ4iqxKgAZkqQdthNji7w" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" wfd-id="id72"></div></div><div data-testid="top-nav-right" class="styles-module__right__mlBQg styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="start" data-padding="normal"><div data-testid="top-bar-actions" class="prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="start" data-padding="none"><div class="styles-module__itemDivider__nunbs hide-sm hide-md"></div><button data-component="Button" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk GlobalCreateMenu-module__actionMenuButton__Hj_iB" data-loading="false" data-size="medium" data-variant="invisible" aria-labelledby="global-create-menu-tooltip-_R_1jpb_" id="_R_5jpb_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></span></span><span data-component="trailingAction" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" aria-hidden="true" id="global-create-menu-tooltip-_R_1jpb_" popover="auto">Create new...</span><div class="hide-sm hide-md prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="start" data-padding="none"><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_m3pb_" href="https://github.com/issues" data-discover="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-issue-opened" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" aria-hidden="true" id="_R_m3pb_" popover="auto">All issues</span><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_q3pb_" href="https://github.com/pulls" data-discover="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" aria-hidden="true" id="_R_q3pb_" popover="auto">All pull requests</span><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_u3pb_" href="https://github.com/repos" data-discover="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-repo" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" aria-hidden="true" id="_R_u3pb_" popover="auto">All repositories</span><div class="d-none"></div></div></div><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ styles-module__notificationIndicator__D_jL0 prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_lpb_" href="https://github.com/notifications" data-discover="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-inbox" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" aria-hidden="true" popover="auto"><span id="_R_lpb_">You have unread notifications<span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->g then n<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true" data-component="Tooltip.KeybindingHintContainer"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">n</span><span aria-hidden="true">N</span></span></kbd></span></span><div class="d-none"></div><div class="GlobalNavUserMenu-module__container__NaVIt"><button data-component="IconButton" type="button" aria-haspopup="menu" data-login="KonstaNtinAleKseeVicHtheonly" class="prc-Button-ButtonBase-9n-Xk GlobalNavUserMenu-module__anchor__Dcej6 prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_2npb_"><img data-component="Avatar" class="prc-Avatar-Avatar-0xaUi" alt="User avatar" width="32" height="32" style="--avatarSize-regular:32px" src="./project_tests_postman_files/163430420" data-testid="github-avatar"></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" aria-hidden="true" id="_R_2npb_" popover="auto">Open user navigation menu</span></div></div></div><h2 class="prc-src-InternalVisuallyHidden-2YaI6">Repository navigation</h2><nav class="prc-components-UnderlineWrapper-eT-Yj LocalNavigation-module__LocalNavigation__b0Xc0" aria-label="Repository" data-variant="inset" data-overflow-measured="true"><ul class="prc-components-UnderlineItemList-xKlKC" role="list"><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s6ptember/fastapi-shop" aria-current="page" data-tab-item="code" data-react-nav="code-view" data-react-nav-anchor="code-view-repo-link" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-code" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></span><span data-component="text" data-content="Code">Code</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s6ptember/fastapi-shop/issues" data-tab-item="issues" data-react-nav="issues-react" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-issue-opened" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg></span><span data-component="text" data-content="Issues">Issues</span><span data-component="counter"><span aria-hidden="true" data-variant="secondary" class="prc-CounterLabel-CounterLabel-X-kRU">1</span><span class="prc-VisuallyHidden-VisuallyHidden-Q0qSB">&nbsp;(<!-- -->1<!-- -->)</span></span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s6ptember/fastapi-shop/pulls" data-tab-item="pull-requests" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg></span><span data-component="text" data-content="Pull requests">Pull requests</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s6ptember/fastapi-shop/actions" data-tab-item="actions" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-play" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path></svg></span><span data-component="text" data-content="Actions">Actions</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s6ptember/fastapi-shop/projects" data-tab-item="projects" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-table" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path></svg></span><span data-component="text" data-content="Projects">Projects</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s6ptember/fastapi-shop/security" data-tab-item="security-and-quality" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-shield" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path></svg></span><span data-component="text" data-content="Security and quality">Security and quality</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/s6ptember/fastapi-shop/pulse" data-tab-item="insights" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-graph" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></span><span data-component="text" data-content="Insights">Insights</span></a></li></ul></nav><div class="d-none"></div></header><script type="application/json" id="__PRIMER_DATA__R_0___">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>


      <div class="js-global-bar" style="display: none;">
        


<qbsearch-input class="search-input" data-scope="repo:s6ptember/fastapi-shop" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="DTvlJAEYdJ6l0lC6nOr2sOeWtMFdVpQm0-8NPq9hbgmU6mcUFZIeMsUYprD3fUhV4GvHi0xQMo7cLh3ssahJOg" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="s6ptember/fastapi-shop" data-current-org="" data-current-owner="s6ptember" data-logged-in="true" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">

    <input type="hidden" name="type" class="js-site-search-type-field" wfd-id="id73">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-3aae17c0-55da-4248-815b-8e7ae9d8580a" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;" wfd-id="id74">
          </div>
        </div>
          <span data-target="query-builder.clearButton" hidden="">
            <span class="sr-only" id="query-builder-test-clear">Clear</span>
            <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-action="
                  click:query-builder#clear
                  focus:query-builder#clearButtonFocus
                  blur:query-builder#clearButtonBlur
                " variant="small" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 tmp-mr-1 px-2 tmp-px-2 py-0 tmp-py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

          </span>
      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                        <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                combobox-commit:query-builder#comboboxCommit
                mousedown:query-builder#resultsMousedown
              " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results" tabindex="-1"></ul>

        </div>
      <div class="FormControl-inlineValidation" id="validation-3aae17c0-55da-4248-815b-8e7ae9d8580a" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted tmp-px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2 tmp-ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2 tmp-ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="utw02nTYashzM42PW_pRH2p3djcNV1lFwKDa9djUfThpRIvSp1f0xqHexCESCp5PoObgBvivAYdss4WldOFewA" wfd-id="id75">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox" wfd-id="id76">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="GzFLobsC3nMfl99kVUqgTfZaJU9XJY2genqS4bwEW3JppHlhSuRDZkFU6CF6vzagz49TJ78eXP9rT4mpglaQNg" wfd-id="id77">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField" wfd-id="id78">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false" wfd-id="id79">
              <input type="hidden" value="rOZ7OPZsmd3xlqhTG90YWU5VcHo_j1c2HJ5xhXOiLM2rGYCwtc5PC9PISf0D33QX0vy9OL4_N9JNhZZEZyvyDw" data-csrf="true" wfd-id="id80">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500" wfd-id="id81">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>  <input type="hidden" value="bxaZrebgw6dEtVHK86L0kqnbMIYn8_DcpT-jv0r_jmkHVKDTR8MKYyC48N7M9OzBYtJ4iqxKgAZkqQdthNji7w" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" wfd-id="id82">


      </div>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md">Reload</a> to refresh your session.</span>

    <button id="icon-button-1c39d6da-70bd-474c-acce-62c940ace844" aria-labelledby="tooltip-2f9b828b-bf71-4a10-ba38-7c28f790252a" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-2f9b828b-bf71-4a10-ba38-7c28f790252a" for="icon-button-1c39d6da-70bd-474c-acce-62c940ace844" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style class="darkreader darkreader--inline" media="screen">[data-darkreader-inline-bgcolor] {
  background-color: var(--darkreader-inline-bgcolor) !important;
}
[data-darkreader-inline-bgimage] {
  background-image: var(--darkreader-inline-bgimage) !important;
}
[data-darkreader-inline-border] {
  border-color: var(--darkreader-inline-border) !important;
}
[data-darkreader-inline-border-bottom] {
  border-bottom-color: var(--darkreader-inline-border-bottom) !important;
}
[data-darkreader-inline-border-left] {
  border-left-color: var(--darkreader-inline-border-left) !important;
}
[data-darkreader-inline-border-right] {
  border-right-color: var(--darkreader-inline-border-right) !important;
}
[data-darkreader-inline-border-top] {
  border-top-color: var(--darkreader-inline-border-top) !important;
}
[data-darkreader-inline-boxshadow] {
  box-shadow: var(--darkreader-inline-boxshadow) !important;
}
[data-darkreader-inline-color] {
  color: var(--darkreader-inline-color) !important;
}
[data-darkreader-inline-fill] {
  fill: var(--darkreader-inline-fill) !important;
}
[data-darkreader-inline-stroke] {
  stroke: var(--darkreader-inline-stroke) !important;
}
[data-darkreader-inline-outline] {
  outline-color: var(--darkreader-inline-outline) !important;
}
[data-darkreader-inline-stopcolor] {
  stop-color: var(--darkreader-inline-stopcolor) !important;
}
[data-darkreader-inline-bg] {
  background: var(--darkreader-inline-bg) !important;
}
[data-darkreader-inline-border-short] {
  border: var(--darkreader-inline-border-short) !important;
}
[data-darkreader-inline-border-bottom-short] {
  border-bottom: var(--darkreader-inline-border-bottom-short) !important;
}
[data-darkreader-inline-border-left-short] {
  border-left: var(--darkreader-inline-border-left-short) !important;
}
[data-darkreader-inline-border-right-short] {
  border-right: var(--darkreader-inline-border-right-short) !important;
}
[data-darkreader-inline-border-top-short] {
  border-top: var(--darkreader-inline-border-top-short) !important;
}
[data-darkreader-inline-invert] {
    filter: invert(100%) hue-rotate(180deg);
}</style><style class="darkreader darkreader--override" media="screen">.vimvixen-hint {
    background-color: var(--darkreader-background-ffd76e, #684b00) !important;
    border-color: var(--darkreader-background-c59d00, #9e7e00) !important;
    color: var(--darkreader-text-302505, #d7d4cf) !important;
}
#vimvixen-console-frame {
    color-scheme: light !important;
}
::placeholder {
    opacity: 0.5 !important;
}
#edge-translate-panel-body,
.MuiTypography-body1,
.nfe-quote-text {
    color: var(--darkreader-neutral-text) !important;
}
gr-main-header {
    background-color: var(--darkreader-background-add8e6, #1b4958) !important;
}
.tou-z65h9k,
.tou-mignzq,
.tou-1b6i2ox,
.tou-lnqlqk {
    background-color: var(--darkreader-neutral-background) !important;
}
.tou-75mvi {
    background-color: var(--darkreader-background-cfecf5, #0f3a47) !important;
}
.tou-ta9e87,
.tou-1w3fhi0,
.tou-1b8t2us,
.tou-py7lfi,
.tou-1lpmd9d,
.tou-1frrtv8,
.tou-17ezmgn {
    background-color: var(--darkreader-background-f5f5f5, #1e2021) !important;
}
.tou-uknfeu {
    background-color: var(--darkreader-background-faedda, #432c09) !important;
}
.tou-6i3zyv {
    background-color: var(--darkreader-background-85c3d8, #245d70) !important;
}
div.mermaid-viewer-control-panel .btn {
    background-color: var(--darkreader-neutral-background);
    fill: var(--darkreader-neutral-text);
}
svg g rect.er {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.entityBox {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.attributeBoxOdd {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.attributeBoxEven {
    fill: var(--darkreader-selection-background);
    fill-opacity: 0.8 !important;
}
svg rect.er.relationshipLabelBox {
    fill: var(--darkreader-neutral-background) !important;
}
svg g g.nodes rect,
svg g g.nodes polygon {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.task {
    fill: var(--darkreader-selection-background) !important;
}
svg line.messageLine0,
svg line.messageLine1 {
    stroke: var(--darkreader-neutral-text) !important;
}
div.mermaid .actor {
    fill: var(--darkreader-neutral-background) !important;
}
mitid-authenticators-code-app > .code-app-container {
    background-color: white !important;
    padding-top: 1rem;
}
iframe#unpaywall[src$="unpaywall.html"] {
    color-scheme: light !important;
}
select {
    --darkreader-bg--form-control-background-color: rgba(22, 22, 22, 0) !important;
}
body#tumblr {
    --darkreader-bg--secondary-accent: 31, 32, 34 !important;
    --darkreader-bg--white: 23, 23, 23 !important;
    --darkreader-text--black: 228, 224, 218 !important;
}
:host {
    --d2l-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-button-icon-background-color-hover: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-color-ferrite: var(--darkreader-neutral-text) !important;
    --d2l-color-sylvite: var(--darkreader-bg--d2l-color-sylvite) !important;
    --d2l-dropdown-background-color: var(--darkreader-neutral-background) !important;
    --d2l-dropdown-border-color: var(--darkreader-border--d2l-color-mica) !important;
    --d2l-input-backgroud-color: var(--darkreader-neutral-background) !important;
    --d2l-menu-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-tooltip-background-color: var(--darkreader-neutral-background) !important;
    --d2l-tooltip-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
:host([_floating]) .d2l-floating-buttons-container {
    background-color: var(--darkreader-neutral-background) !important;
    border-top-color: var(--darkreader-border--d2l-color-mica) !important;
    opacity: 0.88 !important;
}
d2l-card {
    background: var(--darkreader-neutral-background) !important;
    border-color: var(--darkreader-border--d2l-color-gypsum) !important;
}
d2l-dropdown-content > div,
d2l-menu-item {
    background-color: var(--darkreader-neutral-background) !important;
    border-radius: 10px !important;
}
d2l-empty-state-simple {
    border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-button-filter > ul > li > a.vui-button {
    border-color: var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-label-text:has(.d2l-button-subtle-content):hover,
.d2l-label-text:has(.d2l-button-subtle-content):focus,
.d2l-label-text:has(.d2l-button-subtle-content):active {
    background-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-navigation-centerer {
    color: inherit !important;
}
.d2l-tabs-layout {
    border-color: var(--darkreader-border--d2l-color-gypsum) !important;
}
.d2l-input,
.d2l-calendar-date,
.d2l-htmleditor-container {
    background-color: var(--darkreader-neutral-background) !important;
}
.d2l-collapsible-panel {
    border: 1px solid var(--darkreader-border--d2l-color-mica) !important;
    border-radius: 0.4rem !important;
}
.d2l-collapsible-panel-divider {
    border-bottom: 1px solid var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-w2d-flex {
    border-bottom: 2px solid var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-collapsible-panel scrolled,
.d2l-collapsible-panel-header,
.d2l-w2d-collection-fixed {
    background-color: var(--darkreader-neutral-background) !important;
}
.d2l-loading-spinner-bg {
    fill: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-loading-spinner-bg-stroke {
    stroke: var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-loading-spinner-wrapper svg path,
.d2l-loading-spinner-wrapper svg circle {
    fill: var(--darkreader-neutral-background) !important;
}
.d2l-twopanelselector-side.d2l-twopanelselector-side-sep {
    background: var(--darkreader-bg--d2l-color-mica) !important;
}
.d2l-le-TreeAccordionItem-anchor::before {
    background: var(--darkreader-bg--d2l-color-corundum) !important;
}
table[class|="moz-header"] {
    background: none;
}
*[style*="color: rgba(0,0,0,"],
*[style*="color: rgba(0, 0, 0,"],
*[style*="color:#000"],
*[style*="color:black"],
*[style*="color:#282828"],
*[style*="color:#444"] {
    color: var(--darkreader-neutral-text) !important;
}
*[style*="background:#fff"],
*[style*="background-color:#fff"] {
    background: var(--darkreader-neutral-background) !important;
}
*[bgcolor="#F5F5F5"],
*[style*="background-color: #F5F5F5"] {
    background: var(--darkreader-background-f5f5f5, #1e2021) !important;
}
body[style*="background: rgb(255, 255, 255) !important"] *:not(a),
.body[style*="background-color: rgb(254, 254, 254) !important"] *:not(a) {
    background-color: var(--darkreader-neutral-background) !important;
}
div[style*="www.gstatic.com/android/"] {
    background: none !important;
}
*[style*="background:#f9f9f9"] {
    background: var(--darkreader-background-f9f9f9, #1b1e1f) !important;
}
body.mediawiki.skin-vector #mw-page-base {
    background-image: none !important;
}
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
.blob-code-inner,
.blob-num,
.cm-s-github-light .CodeMirror-lines,
.CodeMirror pre > span,
.CodeMirror,
.CodeMirror-dialog input,
.CodeMirror-hints,
.CodeMirror-linenumber,
.CodeMirror-lines,
.commit .sha,
.commit .sha-block,
.commit-desc pre,
.commit-ref,
.commit-tease-sha,
.export-phrase pre,
.file-info,
.FormControl-input.FormControl-monospace,
.FormControl-select.FormControl-monospace,
.FormControl-textarea.FormControl-monospace,
.input-monospace,
.markdown-body .footnotes .data-footnote-backref g-emoji,
.pr-1 > code > a,
.react-blob-print-hide,
.react-code-text,
.react-code-view-edit .cm-s-github-light .CodeMirror-lines,
.text-mono *,
.text-mono,
.two-factor-recovery-codes,
[aria-labelledby*="codemirror"] *,
[class*="blob-code"] *,
code > a[class="Link--secondary"],
section[aria-labelledby*="file-name-id"] > div > div *,
span.commit-ref > a > *,
span.commit-ref > a {
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace !important;
}
.markdown-body code,
.markdown-title code {
    background-color: var(--darkreader-text-1b1f231a, rgba(212, 209, 203, 0.1)) !important;
}
.markdown-body pre code {
    background-color: transparent !important;
}
.refined-github .dashboard .js-all-activity-header + div {
    background-color: var(--darkreader-background-e4e5e9, #26292b) !important;
    border-color: var(--darkreader-background-bbc1c9, #3a3f42) !important;
}
.refined-github .dashboard-rollup-items .body {
    border-top-color: var(--darkreader-background-bbc1c9, #3a3f42) !important;
}
.refined-github .reaction-summary-item a {
    box-shadow: 0 0 0 2px var(--darkreader-background-ffffff, #181a1b) !important;
}
.refined-github button.reaction-summary-item {
    border-bottom: rgb(77, 172, 253) !important;
    border-top-color: rgb(52, 59, 68) !important;
}
.js-site-search-form {
    background-color: #ffffff1a !important;
    border-radius: 2pt !important;
}
.blob-num:not(.cc-coverage-covered-border):not(.cc-coverage-missed-border) {
    border-right: 0 !important;
}
.cc-issue-description {
    color: #24292e !important;
}
.cc-readup-background {
    background-color: rgb(28, 30, 31) !important;
}
.cc-readup-content {
    border-left: 1px solid grey !important;
    color: rgb(216, 214, 208) !important;
}
.cc-readup-content blockquote {
    border-left: 3px solid dimgrey !important;
}
.cc-pr__link-text {
    color: darkgrey !important;
}
.cc-pr__tooltip {
    background-color: rgb(28, 30, 31) !important;
    color: darkgrey !important;
}
.jfk-bubble,
.octotree-sidebar,
.cc-pr__logo,
.cc-octicon,
#network canvas,
img.network-tree {
    filter: invert(94.4%) hue-rotate(180deg) contrast(90%) !important;
}
#commit-activity-detail > svg {
    fill: var(--darkreader-text-000000, #e8e6e3) !important;
}
.ContributionCalendar-day,
.ContributionCalendar-day[data-level="0"] {
    fill: var(--color-calendar-graph-day-bg) !important;
}
.ContributionCalendar-day[data-level="1"] {
    fill: var(--color-calendar-graph-day-L1-bg) !important;
}
.ContributionCalendar-day[data-level="2"] {
    fill: var(--color-calendar-graph-day-L2-bg) !important;
}
.ContributionCalendar-day[data-level="3"] {
    fill: var(--color-calendar-graph-day-L3-bg) !important;
}
.ContributionCalendar-day[data-level="4"] {
    fill: var(--color-calendar-graph-day-L4-bg) !important;
}
.day,
.day[data-Count="0"] {
    fill: var(--color-calendar-graph-day-bg) !important;
}
.day[data-Count="1"] {
    fill: var(--color-calendar-graph-day-L1-bg) !important;
}
.day[data-Count="2"] {
    fill: var(--color-calendar-graph-day-L2-bg) !important;
}
.day[data-Count="3"] {
    fill: var(--color-calendar-graph-day-L3-bg) !important;
}
.day[data-Count="4"] {
    fill: var(--color-calendar-graph-day-L4-bg) !important;
}
:root {
    --color-calendar-graph-day-bg: var(--darkreader-background-ebedf0, #222526) !important;
    --color-calendar-graph-day-L1-bg: var(--darkreader-background-9be9a8, #166634) !important;
    --color-calendar-graph-day-L2-bg: var(--darkreader-background-40c463, #2f9a5f) !important;
    --color-calendar-graph-day-L3-bg: var(--darkreader-background-30a14e, #26813e) !important;
    --color-calendar-graph-day-L4-bg: var(--darkreader-text-216e39, #8bdca4) !important;
    --color-previewable-comment-form-bg: var(--darkreader-neutral-background) !important;
}
.Box-row--yellow {
    background-color: var(--darkreader-background-fffbdd, #362f00) !important;
}
.merge-status-list {
    border-color: var(--darkreader-background-c0c5c7, #3a3e41) !important;
}
.user-has-reacted {
    background-color: rgba(17, 88, 199, 0.2) !important;
}
.hx_IssueLabel,
span[class*="TokenBase"] {
    background: rgba(var(--label-r),var(--label-g),var(--label-b),var(--background-alpha)) !important;
    border-color: hsla(var(--label-h),calc(var(--label-s) * 1%),calc((var(--label-l) + var(--lighten-by)) * 1%),var(--border-alpha)) !important;
    color: hsl(var(--label-h),calc(var(--label-s) * 1%),calc((var(--label-l) + var(--lighten-by)) * 1%)) !important;
}
.header-search-input {
    border: 0 !important;
}
.HeaderMenu-link--sign-in {
    border: 0 !important;
}
.timeline-comment--caret.current-user::after {
    --color-current-user-tip-bg: var(--darkreader-bg--color-box-bg-info) !important;
}
.timeline-comment--caret.current-user::before {
    background-color: var(--darkreader-border--color-box-border-info) !important;
}
@media screen and (min-width: 1012px) {
    markdown-toolbar.border-lg-top-0 {
        border-top: 1px solid var(--darkreader-border--color-border-primary) !important;
    }
}
@media screen and (max-width: 767px) {
    div.tabnav--responsive button.tabnav-tab {
        --color-border-primary: var(--darkreader-border--color-border-primary) !important;
    }
}
.TimelineItem-badge[style^="background-color: var(--color-timeline-merged-bg)"] {
    background-color: var(--color-timeline-merged-bg) !important;
}
.ContributionCalendar-label {
    --color-text-primary: var(--darkreader-neutral-text) !important;
}
article div[style^="background: linear-gradient"] {
    background: linear-gradient(to top, var(--darkreader-bg--color-bg-primary), transparent) !important;
}
.ͼ5 .cm-content,
.ͼ5 .cm-panel.cm-search > button {
    background-color: var(--darkreader-neutral-background) !important;
}</style><style class="darkreader darkreader--invert" media="screen">.jfk-bubble.gtx-bubble, .captcheck_answer_label > input + img, span#closed_text > img[src^="https://www.gstatic.com/images/branding/googlelogo"], span[data-href^="https://www.hcaptcha.com/"] > #icon, img.Wirisformula, a[data-testid="headerMediumLogo"]>svg, .d2l-navigation-link-image-container, .d2l-iframe-loading-container, div.mc-ip-hide[style*="background: rgb(255, 255, 255) !important"], [style*="color: rgb(0, 0, 1) !important;"], [src="https://github.githubassets.com/images/modules/site/icons/footer/github-logo.svg"], [src^="https://github.githubassets.com/images/modules/site/home/community-sponsor-"], [src^="https://github.githubassets.com/images/modules/site/home/community-readme-"], [src^="https://github.githubassets.com/images/modules/site/home/community-discussions-"], [src="https://github.githubassets.com/images/modules/site/home/dependabot-merge.png"], [src="https://github.githubassets.com/images/modules/site/home/dependabot-pr.png"], [src="https://github.githubassets.com/images/modules/site/home/gh-desktop.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-merge.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-comment.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-description.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-screen.png"], [src="https://github.githubassets.com/images/modules/site/home/enterprise-city-w-logos.jpg"], [src="https://github.githubassets.com/images/modules/site/codespaces/codespaces-icon.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/dependency-rust.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/dependency-3.png"], [src^="https://github.githubassets.com/images/modules/site/codespaces/dependencies-"], [src="https://github.githubassets.com/images/modules/site/codespaces/commit-3.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/extensions-1.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/extensions-2.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/commit-workflow.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/workflow-view.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/code.png"], [src="https://github.githubassets.com/images/email/explore/explore-gradient-icon.png"], [src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/collections/learn-to-code/learn-to-code.png"], .js-viewport-aware-video.color-bg-primary.width-full.d-block.codespaces-hero-video, .build-in-animate.position-relative.mb-6-fluid.box-shadow-active-mktg.mx-auto.home-mobile-iphone.build-in-slideY.js-build-in > .js-viewport-aware-video.width-full, .overflow-hidden.position-relative.box-shadow-active-border-mktg.rounded-2-fluid.color-bg-primary.build-in-scale-fade.js-build-in-item, .build-in-animate.overflow-hidden.box-shadow-active-border-mktg.rounded-2-fluid.position-relative.home-workflow-comp.js-build-in-item, .mx-lg-auto.col-lg-7.col-12, #hero-section-brand-heading {
    filter: invert(100%) hue-rotate(180deg) contrast(90%) !important;
}</style><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: min(var(--overlay-width-small), 100vw);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><style class="darkreader darkreader--sync" media="screen"></style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
        
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    
  <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTYzNDMwNDIwIiwidCI6MTc3NzQ3ODcwNH0=--e50d62b144b72a30d07c7fac73c1b5112122b9317eafdb5afc2a0b1b6fc2597b" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst="" data-throttle-delay="5000"></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="" data-project-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
      






    
  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>



<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Mod+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Mod+Alt+," target="_blank" href="https://github.com/codespaces/new/s6ptember/fastapi-shop/tree/master?resume=1">Open in codespace</a>




    
      
    








<react-app app-name="code-view" initial-path="/s6ptember/fastapi-shop/blob/master/backend/app/schemas/cart.py" style="display: block; min-height: calc(100vh - 64px);" data-attempted-ssr="true" data-ssr="true" data-lazy="false" data-alternate="false" data-data-router-enabled="true" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"codeViewBlobRoute":{"csv":null,"csvError":null,"headerInfo":{"toc":null},"issueTemplate":null,"discussionTemplate":null,"richText":null,"richTextTruncated":false,"renderedFileInfo":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"CartItemBase","kind":"class","ident_start":73,"ident_end":85,"extent_start":67,"extent_end":242,"fully_qualified_name":"CartItemBase","ident_utf16":{"start":{"line_number":3,"utf16_col":6},"end":{"line_number":3,"utf16_col":18}},"extent_utf16":{"start":{"line_number":3,"utf16_col":0},"end":{"line_number":5,"utf16_col":85}}},{"name":"product_id","kind":"constant","ident_start":102,"ident_end":112,"extent_start":102,"extent_end":156,"fully_qualified_name":"CartItemBase.product_id","ident_utf16":{"start":{"line_number":4,"utf16_col":4},"end":{"line_number":4,"utf16_col":14}},"extent_utf16":{"start":{"line_number":4,"utf16_col":4},"end":{"line_number":4,"utf16_col":58}}},{"name":"quantity","kind":"constant","ident_start":161,"ident_end":169,"extent_start":161,"extent_end":242,"fully_qualified_name":"CartItemBase.quantity","ident_utf16":{"start":{"line_number":5,"utf16_col":4},"end":{"line_number":5,"utf16_col":12}},"extent_utf16":{"start":{"line_number":5,"utf16_col":4},"end":{"line_number":5,"utf16_col":85}}},{"name":"CartItemCreate","kind":"class","ident_start":250,"ident_end":264,"extent_start":244,"extent_end":288,"fully_qualified_name":"CartItemCreate","ident_utf16":{"start":{"line_number":7,"utf16_col":6},"end":{"line_number":7,"utf16_col":20}},"extent_utf16":{"start":{"line_number":7,"utf16_col":0},"end":{"line_number":8,"utf16_col":8}}},{"name":"CartItemUpdate","kind":"class","ident_start":296,"ident_end":310,"extent_start":290,"extent_end":499,"fully_qualified_name":"CartItemUpdate","ident_utf16":{"start":{"line_number":10,"utf16_col":6},"end":{"line_number":10,"utf16_col":20}},"extent_utf16":{"start":{"line_number":10,"utf16_col":0},"end":{"line_number":13,"utf16_col":80}}},{"name":"product_id","kind":"constant","ident_start":327,"ident_end":337,"extent_start":327,"extent_end":381,"fully_qualified_name":"CartItemUpdate.product_id","ident_utf16":{"start":{"line_number":11,"utf16_col":4},"end":{"line_number":11,"utf16_col":14}},"extent_utf16":{"start":{"line_number":11,"utf16_col":4},"end":{"line_number":11,"utf16_col":58}}},{"name":"quantity","kind":"constant","ident_start":386,"ident_end":394,"extent_start":386,"extent_end":499,"fully_qualified_name":"CartItemUpdate.quantity","ident_utf16":{"start":{"line_number":12,"utf16_col":4},"end":{"line_number":12,"utf16_col":12}},"extent_utf16":{"start":{"line_number":12,"utf16_col":4},"end":{"line_number":13,"utf16_col":80}}},{"name":"CartItem","kind":"class","ident_start":507,"ident_end":515,"extent_start":501,"extent_end":917,"fully_qualified_name":"CartItem","ident_utf16":{"start":{"line_number":15,"utf16_col":6},"end":{"line_number":15,"utf16_col":14}},"extent_utf16":{"start":{"line_number":15,"utf16_col":0},"end":{"line_number":22,"utf16_col":75}}},{"name":"product_id","kind":"constant","ident_start":532,"ident_end":542,"extent_start":532,"extent_end":547,"fully_qualified_name":"CartItem.product_id","ident_utf16":{"start":{"line_number":16,"utf16_col":4},"end":{"line_number":16,"utf16_col":14}},"extent_utf16":{"start":{"line_number":16,"utf16_col":4},"end":{"line_number":16,"utf16_col":19}}},{"name":"name","kind":"constant","ident_start":552,"ident_end":556,"extent_start":552,"extent_end":602,"fully_qualified_name":"CartItem.name","ident_utf16":{"start":{"line_number":17,"utf16_col":4},"end":{"line_number":17,"utf16_col":8}},"extent_utf16":{"start":{"line_number":17,"utf16_col":4},"end":{"line_number":17,"utf16_col":54}}},{"name":"price","kind":"constant","ident_start":607,"ident_end":612,"extent_start":607,"extent_end":661,"fully_qualified_name":"CartItem.price","ident_utf16":{"start":{"line_number":18,"utf16_col":4},"end":{"line_number":18,"utf16_col":9}},"extent_utf16":{"start":{"line_number":18,"utf16_col":4},"end":{"line_number":18,"utf16_col":58}}},{"name":"quantity","kind":"constant","ident_start":666,"ident_end":674,"extent_start":666,"extent_end":724,"fully_qualified_name":"CartItem.quantity","ident_utf16":{"start":{"line_number":19,"utf16_col":4},"end":{"line_number":19,"utf16_col":12}},"extent_utf16":{"start":{"line_number":19,"utf16_col":4},"end":{"line_number":19,"utf16_col":62}}},{"name":"subtotal","kind":"constant","ident_start":729,"ident_end":737,"extent_start":729,"extent_end":841,"fully_qualified_name":"CartItem.subtotal","ident_utf16":{"start":{"line_number":20,"utf16_col":4},"end":{"line_number":20,"utf16_col":12}},"extent_utf16":{"start":{"line_number":20,"utf16_col":4},"end":{"line_number":21,"utf16_col":83}}},{"name":"image_url","kind":"constant","ident_start":846,"ident_end":855,"extent_start":846,"extent_end":917,"fully_qualified_name":"CartItem.image_url","ident_utf16":{"start":{"line_number":22,"utf16_col":4},"end":{"line_number":22,"utf16_col":13}},"extent_utf16":{"start":{"line_number":22,"utf16_col":4},"end":{"line_number":22,"utf16_col":75}}},{"name":"CartResponse","kind":"class","ident_start":925,"ident_end":937,"extent_start":919,"extent_end":1166,"fully_qualified_name":"CartResponse","ident_utf16":{"start":{"line_number":24,"utf16_col":6},"end":{"line_number":24,"utf16_col":18}},"extent_utf16":{"start":{"line_number":24,"utf16_col":0},"end":{"line_number":27,"utf16_col":78}}},{"name":"items","kind":"constant","ident_start":954,"ident_end":959,"extent_start":954,"extent_end":1025,"fully_qualified_name":"CartResponse.items","ident_utf16":{"start":{"line_number":25,"utf16_col":4},"end":{"line_number":25,"utf16_col":9}},"extent_utf16":{"start":{"line_number":25,"utf16_col":4},"end":{"line_number":25,"utf16_col":75}}},{"name":"total","kind":"constant","ident_start":1030,"ident_end":1035,"extent_start":1030,"extent_end":1087,"fully_qualified_name":"CartResponse.total","ident_utf16":{"start":{"line_number":26,"utf16_col":4},"end":{"line_number":26,"utf16_col":9}},"extent_utf16":{"start":{"line_number":26,"utf16_col":4},"end":{"line_number":26,"utf16_col":61}}},{"name":"items_count","kind":"constant","ident_start":1092,"ident_end":1103,"extent_start":1092,"extent_end":1166,"fully_qualified_name":"CartResponse.items_count","ident_utf16":{"start":{"line_number":27,"utf16_col":4},"end":{"line_number":27,"utf16_col":15}},"extent_utf16":{"start":{"line_number":27,"utf16_col":4},"end":{"line_number":27,"utf16_col":78}}}]}},"codeViewLayoutRoute":{"repo":{"id":1075982471,"defaultBranch":"master","name":"fastapi-shop","ownerLogin":"s6ptember","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2025-10-14T11:46:21.000+03:00","ownerAvatar":"https://avatars.githubusercontent.com/u/190271353?v=4","public":true,"private":false,"isOrgOwned":false},"currentUser":{"id":163430420,"login":"KonstaNtinAleKseeVicHtheonly","userEmail":"ept.13@inbox.ru"},"uploadToken":"zQpGk7LOBOQh01HpuwqZG8kxQ_esZftKOc9B6CeWaaTwfFMhhjLZ7qzjjx6zhveKvO29Myu_ULDHofdovtfZJQ","allShortcutsEnabled":true,"treeExpanded":true,"path":"backend/app/schemas/cart.py","symbolsExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1760431712.0","canEdit":false,"currentOid":"dc2b28b67df5c1408520dc025da54437d4674c67"},"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-378c581dbdb2429c.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-82470c2dd86b326d.js","githubDevUrl":"https://github.dev/"},"codeViewFileTreeLayoutRoute":{"fileTree":{"backend/app/schemas":{"items":[{"name":"__init__.py","path":"backend/app/schemas/__init__.py","contentType":"file"},{"name":"cart.py","path":"backend/app/schemas/cart.py","contentType":"file"},{"name":"category.py","path":"backend/app/schemas/category.py","contentType":"file"},{"name":"product.py","path":"backend/app/schemas/product.py","contentType":"file"}],"totalCount":4},"backend/app":{"items":[{"name":"models","path":"backend/app/models","contentType":"directory"},{"name":"repositories","path":"backend/app/repositories","contentType":"directory"},{"name":"routes","path":"backend/app/routes","contentType":"directory"},{"name":"schemas","path":"backend/app/schemas","contentType":"directory"},{"name":"services","path":"backend/app/services","contentType":"directory"},{"name":"__init__.py","path":"backend/app/__init__.py","contentType":"file"},{"name":"config.py","path":"backend/app/config.py","contentType":"file"},{"name":"database.py","path":"backend/app/database.py","contentType":"file"},{"name":"main.py","path":"backend/app/main.py","contentType":"file"}],"totalCount":9},"backend":{"items":[{"name":"app","path":"backend/app","contentType":"directory"},{"name":"static","path":"backend/static","contentType":"directory"},{"name":"Dockerfile","path":"backend/Dockerfile","contentType":"file"},{"name":"requirements.txt","path":"backend/requirements.txt","contentType":"file"},{"name":"run.py","path":"backend/run.py","contentType":"file"},{"name":"seed_data.py","path":"backend/seed_data.py","contentType":"file"},{"name":"shop.db","path":"backend/shop.db","contentType":"file"},{"name":"test_commands.md","path":"backend/test_commands.md","contentType":"file"}],"totalCount":8},"":{"items":[{"name":"backend","path":"backend","contentType":"directory"},{"name":"frontend","path":"frontend","contentType":"directory"},{"name":"nginx","path":"nginx","contentType":"directory"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"deploy.sh","path":"deploy.sh","contentType":"file"},{"name":"docker-compose.yml","path":"docker-compose.yml","contentType":"file"}],"totalCount":7}},"fileTreeProcessingTime":152.811817,"foldersToFetch":[]},"codeViewBlobLayoutRoute":{"codeLineWrapEnabled":false,"refInfo":{"name":"master","listCacheKey":"v0:1760431712.0","canEdit":true,"refType":"branch","currentOid":"dc2b28b67df5c1408520dc025da54437d4674c67","canEditOnDefaultBranch":true,"fileExistsOnDefault":true},"path":"backend/app/schemas/cart.py","blob":{"copilotSWEAgentEnabled":false,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/s6ptember/fastapi-shop/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false},"displayName":"cart.py","displayUrl":"https://github.com/s6ptember/fastapi-shop/blob/master/backend/app/schemas/cart.py?raw=true","headerInfo":{"blobSize":"1.14 KB","deleteTooltip":"Fork this repository and delete the file","editTooltip":"Fork this repository and edit the file","ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"onBranch":true,"shortPath":"e5f65bf","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fs6ptember%2Ffastapi-shop%2Fblob%2Fmaster%2Fbackend%2Fapp%2Fschemas%2Fcart.py","isCSV":false,"isRichtext":false,"lineInfo":{"truncatedLoc":"28","truncatedSloc":"23"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"isIssueTemplate":false,"isDiscussionTemplate":false,"language":"Python","languageID":303,"large":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/s6ptember/fastapi-shop/blob/master/backend/app/schemas/cart.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/s6ptember/fastapi-shop/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/s6ptember/fastapi-shop/raw/refs/heads/master/backend/app/schemas/cart.py","renderImageOrRaw":false,"shortPath":null,"symbolsEnabled":true,"tabSize":4,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"copilotSpacesEnabled":false,"modelsAccessAllowed":false,"modelsRepoIntegrationEnabled":false,"isMarketplaceEnabled":true},"codeViewBlobLayoutRoute.StyledBlob":{"rawLines":["from pydantic import BaseModel, Field","from typing import Optional","","class CartItemBase(BaseModel):","    product_id: int = Field(..., description=\"Product ID\")","    quantity: int = Field(..., gt=0, description=\"Quantity (must be greater than 0)\")","","class CartItemCreate(CartItemBase):","    pass","","class CartItemUpdate(BaseModel):","    product_id: int = Field(..., description=\"Product ID\")","    quantity: int = Field(..., gt=0,","                            description=\"New quantity (must be greater than 0)\")","","class CartItem(BaseModel):","    product_id: int","    name: str = Field(..., description=\"Product name\")","    price: float = Field(..., description=\"Product price\")","    quantity: int = Field(..., description=\"Quantity in cart\")","    subtotal: float = Field(...,","                        description=\"Total price for this item (price * quantity)\")","    image_url: Optional[str] = Field(None, description=\"Product image URL\")","","class CartResponse(BaseModel):","    items: list[CartItem] = Field(..., description=\"List of items in cart\")","    total: float = Field(..., description=\"Total cart price\")","    items_count: int = Field(..., description=\"Total number of items in cart\")"],"stylingDirectives":null,"colorizedLines":["\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003epydantic\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-v\u003eBaseModel\u003c/span\u003e, \u003cspan class=pl-v\u003eField\u003c/span\u003e","\u003cspan class=pl-k\u003efrom\u003c/span\u003e \u003cspan class=pl-s1\u003etyping\u003c/span\u003e \u003cspan class=pl-k\u003eimport\u003c/span\u003e \u003cspan class=pl-v\u003eOptional\u003c/span\u003e","","\u003cspan class=pl-k\u003eclass\u003c/span\u003e \u003cspan class=pl-v\u003eCartItemBase\u003c/span\u003e(\u003cspan class=pl-v\u003eBaseModel\u003c/span\u003e):","    \u003cspan class=pl-s1\u003eproduct_id\u003c/span\u003e: \u003cspan class=pl-smi\u003eint\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(..., \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;Product ID\u0026quot;\u003c/span\u003e)","    \u003cspan class=pl-s1\u003equantity\u003c/span\u003e: \u003cspan class=pl-smi\u003eint\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(..., \u003cspan class=pl-s1\u003egt\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-c1\u003e0\u003c/span\u003e, \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;Quantity (must be greater than 0)\u0026quot;\u003c/span\u003e)","","\u003cspan class=pl-k\u003eclass\u003c/span\u003e \u003cspan class=pl-v\u003eCartItemCreate\u003c/span\u003e(\u003cspan class=pl-v\u003eCartItemBase\u003c/span\u003e):","    \u003cspan class=pl-k\u003epass\u003c/span\u003e","","\u003cspan class=pl-k\u003eclass\u003c/span\u003e \u003cspan class=pl-v\u003eCartItemUpdate\u003c/span\u003e(\u003cspan class=pl-v\u003eBaseModel\u003c/span\u003e):","    \u003cspan class=pl-s1\u003eproduct_id\u003c/span\u003e: \u003cspan class=pl-smi\u003eint\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(..., \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;Product ID\u0026quot;\u003c/span\u003e)","    \u003cspan class=pl-s1\u003equantity\u003c/span\u003e: \u003cspan class=pl-smi\u003eint\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(..., \u003cspan class=pl-s1\u003egt\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-c1\u003e0\u003c/span\u003e,","                            \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;New quantity (must be greater than 0)\u0026quot;\u003c/span\u003e)","","\u003cspan class=pl-k\u003eclass\u003c/span\u003e \u003cspan class=pl-v\u003eCartItem\u003c/span\u003e(\u003cspan class=pl-v\u003eBaseModel\u003c/span\u003e):","    \u003cspan class=pl-s1\u003eproduct_id\u003c/span\u003e: \u003cspan class=pl-smi\u003eint\u003c/span\u003e","    \u003cspan class=pl-s1\u003ename\u003c/span\u003e: \u003cspan class=pl-smi\u003estr\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(..., \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;Product name\u0026quot;\u003c/span\u003e)","    \u003cspan class=pl-s1\u003eprice\u003c/span\u003e: \u003cspan class=pl-smi\u003efloat\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(..., \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;Product price\u0026quot;\u003c/span\u003e)","    \u003cspan class=pl-s1\u003equantity\u003c/span\u003e: \u003cspan class=pl-smi\u003eint\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(..., \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;Quantity in cart\u0026quot;\u003c/span\u003e)","    \u003cspan class=pl-s1\u003esubtotal\u003c/span\u003e: \u003cspan class=pl-smi\u003efloat\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(...,","                        \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;Total price for this item (price * quantity)\u0026quot;\u003c/span\u003e)","    \u003cspan class=pl-s1\u003eimage_url\u003c/span\u003e: \u003cspan class=pl-v\u003eOptional\u003c/span\u003e[\u003cspan class=pl-smi\u003estr\u003c/span\u003e] \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(\u003cspan class=pl-c1\u003eNone\u003c/span\u003e, \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;Product image URL\u0026quot;\u003c/span\u003e)","","\u003cspan class=pl-k\u003eclass\u003c/span\u003e \u003cspan class=pl-v\u003eCartResponse\u003c/span\u003e(\u003cspan class=pl-v\u003eBaseModel\u003c/span\u003e):","    \u003cspan class=pl-s1\u003eitems\u003c/span\u003e: \u003cspan class=pl-s1\u003elist\u003c/span\u003e[\u003cspan class=pl-smi\u003eCartItem\u003c/span\u003e] \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(..., \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;List of items in cart\u0026quot;\u003c/span\u003e)","    \u003cspan class=pl-s1\u003etotal\u003c/span\u003e: \u003cspan class=pl-smi\u003efloat\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(..., \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;Total cart price\u0026quot;\u003c/span\u003e)","    \u003cspan class=pl-s1\u003eitems_count\u003c/span\u003e: \u003cspan class=pl-smi\u003eint\u003c/span\u003e \u003cspan class=pl-c1\u003e=\u003c/span\u003e \u003cspan class=pl-en\u003eField\u003c/span\u003e(..., \u003cspan class=pl-s1\u003edescription\u003c/span\u003e\u003cspan class=pl-c1\u003e=\u003c/span\u003e\u003cspan class=pl-s\u003e\u0026quot;Total number of items in cart\u0026quot;\u003c/span\u003e)"]}},"title":"fastapi-shop/backend/app/schemas/cart.py at master · s6ptember/fastapi-shop","appPayload":{},"meta":{"title":"fastapi-shop/backend/app/schemas/cart.py at master · s6ptember/fastapi-shop"}}</script>
  <div data-target="react-app.reactRoot"><meta name="github-code-view-meta-stats" id="github-code-view-meta-stats" data-hydrostats="publish"> <!-- --> <a hidden="" id="code-view-repo-link" href="https://github.com/s6ptember/fastapi-shop" data-discover="true"></a> <div class="d-none"></div><div><div style="--spacing:var(--spacing-none)" class="prc-PageLayout-PageLayoutRoot--KH-d"><div class="prc-PageLayout-PageLayoutWrapper-2BhU2" data-width="full"><div class="prc-PageLayout-PageLayoutContent-BneH9"><div class="CodeViewFileTreeLayout-module__sidebar__n_Aau" tabindex="0"><div class="prc-PageLayout-PaneWrapper-pHPop ReposFileTreePane-module__Pane__rBZpI ReposFileTreePane-module__HidePane__VHAVt" style="--offset-header:0px;--spacing-row:var(--spacing-none);--spacing-column:var(--spacing-none)" data-is-hidden="false" data-position="start" data-sticky="true"><div class="prc-PageLayout-HorizontalDivider-JLVqp prc-PageLayout-PaneHorizontalDivider-9tbnE" data-variant-regular="none" data-variant-narrow="none" data-position="start" style="--spacing-divider:var(--spacing-none);--spacing:var(--spacing-none)"></div><div class="prc-PageLayout-Pane-AyzHK" data-resizable="true" style="--spacing: var(--spacing-none); --pane-min-width: 256px; --pane-max-width: 577px; --pane-width-size: var(--pane-width-large); --pane-width: 320px;"><div><div id="repos-file-tree" class="ReposFileTreePane-module__PaneContents__SJjfF"><div class="ReposFileTreePane-module__Box_1__PpIop"><div class="d-flex width-full tmp-mb-3 flex-items-center"><h2 class="use-tree-pane-module__Heading__s4QbZ prc-Heading-Heading-MtWFE"><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-expanded="true" aria-controls="repos-file-tree" class="prc-Button-ButtonBase-9n-Xk position-relative ExpandFileTreeButton-module__expandButton__hDOcv fgColor-muted prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_ijbd3al1d_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="se" data-component="Tooltip" aria-hidden="true" id="_R_ijbd3al1d_" popover="auto" style="top: 152px; left: 16px;">Collapse file tree</span><div class="d-none"></div></h2><h2 class="CodeViewFileTreeLayout-module__heading__A1Iqk">Files</h2></div><div class="ReposFileTreePane-module__Box_2__g74WI"><div class="ReposFileTreePane-module__Box_3__D6cTp"><button data-component="Button" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" style="min-width:0" aria-label="master branch" data-testid="anchor-button" data-icv-name="Switch branches/tags" class="prc-Button-ButtonBase-9n-Xk react-repos-tree-pane-ref-selector width-full ref-selector-class RefSelectorAnchoredOverlay-module__RefSelectorOverlayBtn__a3WK3" data-loading="false" data-size="medium" data-variant="default" id="ref-picker-repos-header-ref-selector"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayContainer__yaf4p"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayHeader__XtXRG"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="ref-selector-button-text-container RefSelectorAnchoredOverlay-module__RefSelectorBtnTextContainer__Di3rk"><span class="RefSelectorAnchoredOverlay-module__RefSelectorText__w_fmP">&nbsp;<!-- -->master</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><div class="d-none"></div></div><div class="ReposFileTreePane-module__Box_4__DG4pa"><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk ReposFileTreePane-module__IconButton__rGggU prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_r_3g_" href="https://github.com/s6ptember/fastapi-shop/new/master/backend" data-discover="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" data-component="Tooltip" aria-hidden="true" id="_r_3g_" popover="auto">Add file</span><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk SearchButton-module__IconButton__SBlqu ReposFileTreePane-module__SearchButtonWithLeftBorder__TBrDc prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_R_l3bd3al1d_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" data-component="Tooltip" aria-hidden="true" popover="auto"><span id="_R_l3bd3al1d_">Search this repository<span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->forward slash<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true" data-component="Tooltip.KeybindingHintContainer"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">forward slash</span><span aria-hidden="true">/</span></span></kbd></span></span></div></div></div><div class="ReposFileTreePane-module__FileResultsList__zmSnM"><span class="d-flex FileResultsList-module__FilesSearchBox__ivVkc TextInput-wrapper prc-components-TextInputWrapper-Hpdqi prc-components-TextInputBaseWrapper-wY-n0" data-component="TextInput" data-leading-visual="true" aria-busy="false" data-trailing-action="true"><span class="TextInput-icon" id="_R_2lbd3al1d_" aria-hidden="true" data-component="TextInput.LeadingVisual"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" aria-describedby="_R_2lbd3al1d_" data-component="input" class="prc-components-Input-IwWrt" value="test" wfd-id="id83"><span class="TextInput-action prc-components-TextInputAction-CjGDX" data-component="TextInput.Action"><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk prc-components-Invisible-bKOcl fgColor-muted prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_r_7o_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-x-circle-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" aria-hidden="true" id="_r_7o_" popover="auto">Clear</span></span></span></div><div class="d-none"></div><div class="ReposFileTreePane-module__Box_5__Zy_o6"><div style="height:1px;margin-top:-1px;width:100%;flex-shrink:0"></div><div><div class="react-tree-show-tree-items-on-large-screen"><div class="ReposFileTreeView-module__Box__vkb5W" data-testid="repos-file-tree-container"><nav aria-label="File Tree Navigation"><span class="prc-src-InternalVisuallyHidden-2YaI6"><div>nginx content loaded</div></span><ul role="tree" aria-label="Files" data-truncate-text="true" class="prc-TreeView-TreeViewRootUlStyles-Mzrmj"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="backend-item" role="treeitem" aria-labelledby="_r_0_" aria-describedby="_r_1_" aria-level="1" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_0_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_1_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file-directory-open-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M.513 1.513A1.75 1.75 0 0 1 1.75 1h3.5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1H13a1 1 0 0 1 1 1v.5H2.75a.75.75 0 0 0 0 1.5h11.978a1 1 0 0 1 .994 1.117L15 13.25A1.75 1.75 0 0 1 13.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75c0-.464.184-.91.513-1.237Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>backend</span></span></div></div><ul role="group" aria-label="backend" style="list-style: none; padding: 0px; margin: 0px;"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="backend/app-item" role="treeitem" aria-labelledby="_r_av_" aria-describedby="_r_b0_" aria-level="2" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_av_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_b0_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>app</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="backend/static/images-item" role="treeitem" aria-labelledby="_r_b3_" aria-describedby="_r_b4_" aria-level="2" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_b3_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_b4_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>static/images</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="backend/Dockerfile-item" role="treeitem" aria-labelledby="_r_b7_" aria-describedby="_r_b8_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_b7_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_b8_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>Dockerfile</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="backend/requirements.txt-item" role="treeitem" aria-labelledby="_r_bb_" aria-describedby="_r_bc_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_bb_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_bc_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>requirements.txt</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="backend/run.py-item" role="treeitem" aria-labelledby="_r_bf_" aria-describedby="_r_bg_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_bf_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_bg_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>run.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="backend/seed_data.py-item" role="treeitem" aria-labelledby="_r_bj_" aria-describedby="_r_bk_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_bj_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_bk_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>seed_data.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="backend/shop.db-item" role="treeitem" aria-labelledby="_r_bn_" aria-describedby="_r_bo_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_bn_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_bo_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>shop.db</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="0" id="backend/test_commands.md-item" role="treeitem" aria-labelledby="_r_br_" aria-describedby="_r_bs_" aria-level="2" aria-selected="false" aria-current="true"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_br_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_bs_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>test_commands.md</span></span></div></div></li></ul></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend-item" role="treeitem" aria-labelledby="_r_2o_" aria-describedby="_r_2p_" aria-level="1" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_2o_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_2p_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file-directory-open-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M.513 1.513A1.75 1.75 0 0 1 1.75 1h3.5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1H13a1 1 0 0 1 1 1v.5H2.75a.75.75 0 0 0 0 1.5h11.978a1 1 0 0 1 .994 1.117L15 13.25A1.75 1.75 0 0 1 13.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75c0-.464.184-.91.513-1.237Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>frontend</span></span></div></div><ul role="group" aria-label="frontend" style="list-style: none; padding: 0px; margin: 0px;"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/public-item" role="treeitem" aria-labelledby="_r_md_" aria-describedby="_r_me_" aria-level="2" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_md_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_me_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>public</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/src-item" role="treeitem" aria-labelledby="_r_mh_" aria-describedby="_r_mi_" aria-level="2" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_mh_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_mi_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>src</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/.editorconfig-item" role="treeitem" aria-labelledby="_r_ml_" aria-describedby="_r_mm_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_ml_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_mm_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>.editorconfig</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/.gitattributes-item" role="treeitem" aria-labelledby="_r_mp_" aria-describedby="_r_mq_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_mp_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_mq_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>.gitattributes</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/.gitignore-item" role="treeitem" aria-labelledby="_r_mt_" aria-describedby="_r_mu_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_mt_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_mu_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>.gitignore</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/.prettierrc.json-item" role="treeitem" aria-labelledby="_r_n1_" aria-describedby="_r_n2_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_n1_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_n2_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>.prettierrc.json</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/Dockerfile-item" role="treeitem" aria-labelledby="_r_n5_" aria-describedby="_r_n6_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_n5_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_n6_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>Dockerfile</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/README.md-item" role="treeitem" aria-labelledby="_r_n9_" aria-describedby="_r_na_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_n9_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_na_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>README.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/eslint.config.js-item" role="treeitem" aria-labelledby="_r_nd_" aria-describedby="_r_ne_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_nd_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_ne_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>eslint.config.js</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/index.html-item" role="treeitem" aria-labelledby="_r_nh_" aria-describedby="_r_ni_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_nh_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_ni_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>index.html</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/jsconfig.json-item" role="treeitem" aria-labelledby="_r_nl_" aria-describedby="_r_nm_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_nl_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_nm_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>jsconfig.json</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/nginx.conf-item" role="treeitem" aria-labelledby="_r_np_" aria-describedby="_r_nq_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_np_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_nq_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>nginx.conf</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/package-lock.json-item" role="treeitem" aria-labelledby="_r_nt_" aria-describedby="_r_nu_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_nt_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_nu_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>package-lock.json</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/package.json-item" role="treeitem" aria-labelledby="_r_o1_" aria-describedby="_r_o2_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_o1_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_o2_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>package.json</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="frontend/vite.config.js-item" role="treeitem" aria-labelledby="_r_o5_" aria-describedby="_r_o6_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_o5_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_o6_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>vite.config.js</span></span></div></div></li></ul></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="nginx-item" role="treeitem" aria-labelledby="_r_2s_" aria-describedby="_r_2t_" aria-level="1" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_2s_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_2t_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file-directory-open-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M.513 1.513A1.75 1.75 0 0 1 1.75 1h3.5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1H13a1 1 0 0 1 1 1v.5H2.75a.75.75 0 0 0 0 1.5h11.978a1 1 0 0 1 .994 1.117L15 13.25A1.75 1.75 0 0 1 13.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75c0-.464.184-.91.513-1.237Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>nginx</span></span></div></div><ul role="group" aria-label="nginx" style="list-style: none; padding: 0px; margin: 0px;"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="nginx/nginx.conf-item" role="treeitem" aria-labelledby="_r_go_" aria-describedby="_r_gp_" aria-level="2" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_go_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_gp_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>nginx.conf</span></span></div></div></li></ul></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id=".gitignore-item" role="treeitem" aria-labelledby="_r_30_" aria-describedby="_r_31_" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id="_r_30_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_31_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>.gitignore</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="README.md-item" role="treeitem" aria-labelledby="_r_34_" aria-describedby="_r_35_" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id="_r_34_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_35_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>README.md</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="deploy.sh-item" role="treeitem" aria-labelledby="_r_38_" aria-describedby="_r_39_" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id="_r_38_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_39_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>deploy.sh</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="docker-compose.yml-item" role="treeitem" aria-labelledby="_r_3c_" aria-describedby="_r_3d_" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id="_r_3c_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_3d_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>docker-compose.yml</span></span></div></div></li></ul></nav></div></div></div></div></div></div></div><div class="prc-PageLayout-VerticalDivider-9QRmK prc-PageLayout-PaneVerticalDivider-le57g" data-variant-narrow="none" data-variant-regular="line" data-variant-wide="line" data-position="start" style="--spacing:var(--spacing-none)"><div class="prc-PageLayout-DraggableHandle-9s6B4" role="slider" aria-label="Draggable pane splitter" aria-valuemin="256" aria-valuemax="577" aria-valuenow="320" aria-valuetext="Pane width 320 pixels" tabindex="0"></div></div></div></div><div class="prc-PageLayout-ContentWrapper-gR9eG" data-is-hidden-narrow="true"><div class="prc-PageLayout-Content-xWL-A" data-width="full" style="--spacing:var(--spacing-none)"><div class="SharedPageLayout-module__content__IwGAp" data-selector="repos-split-pane-content" tabindex="0"><!-- --><!-- -->  <div class="container CodeViewHeader-module__Box__JkPOb"><div class="CodeViewHeader-module__StickyHeader__Qn7UN" id="StickyHeader" style="position: sticky;"><div class="CodeViewHeader-module__Box_1__SbNDV"><div class="CodeViewHeader-module__Box_2__TB46f"><div class="CodeViewHeader-module__Box_6__qKUtX"><div class="Breadcrumb-module__container__Vxvev Breadcrumb-module__lg__Rjz0A"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb--wide-heading" id="repos-header-breadcrumb--wide" class="Breadcrumb-module__nav__rQFDj"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading" id="repos-header-breadcrumb--wide-heading">Breadcrumbs</h2><ol class="Breadcrumb-module__list__ZH6zr"><li class="Breadcrumb-module__listItem__Ib0x_"><a class="Breadcrumb-module__repoLink__O2Nbs prc-Link-Link-9ZwDx" data-component="Link" data-testid="breadcrumbs-repo-link" href="https://github.com/s6ptember/fastapi-shop/tree/master" data-discover="true">fastapi-shop</a></li><li class="Breadcrumb-module__listItem__Ib0x_"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__lg__Rjz0A" aria-hidden="true">/</span><a class="Breadcrumb-module__directoryLink__kQy_t prc-Link-Link-9ZwDx" data-component="Link" href="https://github.com/s6ptember/fastapi-shop/tree/master/backend" data-discover="true">backend</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Breadcrumb-module__filename__equZR"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__lg__Rjz0A" aria-hidden="true">/</span><h1 class="Breadcrumb-module__filenameHeading__MNMtw Breadcrumb-module__lg__Rjz0A prc-Heading-Heading-MtWFE" tabindex="-1" id="file-name-id-wide">test_commands.md</h1></div><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk ml-2 prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_r_o9_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="CopyToClipboardButton-module__tooltip__BhMvU prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" data-component="Tooltip" aria-label="Copy path" aria-hidden="true" id="_r_o9_" popover="auto">Copy path</span></div></div><div class="react-code-view-header-element--wide"><div class="CodeViewHeader-module__Box_7___0R6c"><div class="d-flex gap-2"><button data-component="Button" type="button" class="prc-Button-ButtonBase-9n-Xk NavigationMenu-module__Button__LpKgm" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" style="display: none;"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Blame</span></span></button><div class="d-none"></div><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-wide" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk js-blob-dropdown-click NavigationMenu-module__IconButton__HpX3G prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_r_oh_" id="_r_oe_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" data-component="Tooltip" aria-hidden="true" id="_r_oh_" popover="auto">More file actions</span></div></div></div><div class="react-code-view-header-element--narrow"><div class="CodeViewHeader-module__Box_7___0R6c"><div class="d-flex gap-2"><button data-component="Button" type="button" class="prc-Button-ButtonBase-9n-Xk NavigationMenu-module__Button__LpKgm" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" style="display: none;"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Blame</span></span></button><div class="d-none"></div><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-narrow" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk js-blob-dropdown-click NavigationMenu-module__IconButton__HpX3G prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_r_oo_" id="_r_ol_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" data-component="Tooltip" aria-hidden="true" id="_r_oo_" popover="auto">More file actions</span></div></div></div></div></div></div></div><div class="CodeView-module__contentWrapper__cG2JH"><div class="react-code-view-bottom-padding"><div class="BlobTopBanners-module__Box__v_nvx"></div></div> <div class="d-none"></div><div class="d-flex flex-column border rounded-2 tmp-mb-3 pl-1"><div class="LatestCommit-module__Box__B25ZT"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="LatestCommit-module__Box_1__YkEgg"><div class="CommitAttribution-module__CommitAttributionContainer__I_rfs"><span data-component="AvatarStack" data-variant="cascade" data-shape="circle" data-avatar-count="3" data-responsive="" class="pc-AvatarStack--variant pc-AvatarStack--shape pc-AvatarStack--three prc-AvatarStack-AvatarStack-vkIK2" style="--stackSize-narrow: 20px; --stackSize-regular: 20px; --stackSize-wide: 20px;"><div data-component="AvatarStack.Body" class="pc-AvatarStackBody prc-AvatarStack-AvatarStackBody-JFK4u" tabindex="0"> <img data-component="Avatar" class="pc-AvatarItem prc-AvatarStack-AvatarItem-70eW3 prc-Avatar-Avatar-0xaUi" alt="september" width="20" height="20" data-testid="commit-stack-avatar" src="./project_tests_postman_files/gravatar-user-420.png" style="--avatarSize-regular: 20px;"><img data-component="Avatar" class="pc-AvatarItem prc-AvatarStack-AvatarItem-70eW3 prc-Avatar-Avatar-0xaUi" alt="september" width="20" height="20" data-testid="commit-stack-avatar" src="./project_tests_postman_files/gravatar-user-420.png" style="--avatarSize-regular: 20px;"></div></span><div data-testid="author-link" class="AuthorLink-module__authorLinkContainer__RsptC CommitAttribution-module__AuthorLink__DV7CP"><div class="AuthorDisplayName-module__truncate__d1MRu prc-Truncate-Truncate-2G1eo" data-inline="true" title="september" style="--truncate-max-width: 125px;"><span class="AuthorDisplayName-module__Text__OP5Q9" style="--author-font-weight: var(--base-text-weight-semibold); --author-font-color: var(--fgColor-default); --darkreader-text--author-font-color: var(--darkreader-text--fgColor-default);">september</span></div></div><span class="pl-1">and</span><div data-testid="author-link" class="AuthorLink-module__authorLinkContainer__RsptC CommitAttribution-module__AuthorLink__DV7CP"><div class="AuthorDisplayName-module__truncate__d1MRu prc-Truncate-Truncate-2G1eo" data-inline="true" title="september" style="--truncate-max-width: 125px;"><span class="AuthorDisplayName-module__Text__OP5Q9" style="--author-font-weight: var(--base-text-weight-semibold); --author-font-color: var(--fgColor-default); --darkreader-text--author-font-color: var(--darkreader-text--fgColor-default);">september</span></div></div><span class=""></span></div><div class="d-none d-sm-flex LatestCommit-module__Box_2__pSPKJ"><div class="Truncate flex-items-center f5"><span class="Truncate-text prc-Text-Text-9mHv3" data-testid="latest-commit-html"><a data-hovercard-url="/s6ptember/fastapi-shop/commit/01c934a0fd5d651460998559f1ee99ba38b00656/hovercard" data-pjax="true" class="Link--secondary" href="https://github.com/s6ptember/fastapi-shop/commit/01c934a0fd5d651460998559f1ee99ba38b00656" aria-keyshortcuts="Alt+ArrowUp">add test command(with ai)</a></span></div></div><span class="d-flex d-sm-none fgColor-muted f6"><relative-time tense="past" datetime="2025-10-17T12:06:19.000Z" title="Oct 17, 2025, 3:06 PM GMT+3"><template shadowrootmode="open">6 months ago</template>Oct 17, 2025</relative-time></span></div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"><span class="d-flex flex-nowrap fgColor-muted f6"><a class="Link--secondary prc-Link-Link-9ZwDx" data-component="Link" aria-label="Commit 01c934a" data-hovercard-url="/s6ptember/fastapi-shop/commit/01c934a0fd5d651460998559f1ee99ba38b00656/hovercard" data-hovercard-type="commit" octo-click="hovercard-link-click" octo-dimensions="link_type:self" aria-keyshortcuts="Alt+ArrowUp" href="https://github.com/s6ptember/fastapi-shop/commit/01c934a0fd5d651460998559f1ee99ba38b00656" data-discover="true">01c934a</a>&nbsp;·&nbsp;<relative-time tense="past" datetime="2025-10-17T12:06:19.000Z" title="Oct 17, 2025, 3:06 PM GMT+3"><template shadowrootmode="open">6 months ago</template>Oct 17, 2025</relative-time></span></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">History</h2><a data-component="LinkButton" href="https://github.com/s6ptember/fastapi-shop/commits/master/backend/test_commands.md" class="prc-Button-ButtonBase-9n-Xk d-none d-lg-flex LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="fgColor-default">History</span></span></span></a><div class="d-sm-none"><button data-component="IconButton" type="button" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" class="prc-Button-ButtonBase-9n-Xk LatestCommit-module__IconButton__mkJr_ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_r_os_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" aria-hidden="true" id="_r_os_" popover="auto">Open commit details</span></div><div class="d-flex d-lg-none"><a data-component="LinkButton" aria-label="View commit history for this file." href="https://github.com/s6ptember/fastapi-shop/commits/master/backend/test_commands.md" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby="_r_ou_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" data-component="Tooltip" role="tooltip" aria-hidden="true" id="_r_ou_" popover="auto">History</span></div></div></div></div></div><div class="d-flex flex-row"><div class="container BlobViewContent-module__blobContainer__DtH2d"><div class="react-code-size-details-banner BlobViewContent-module__codeSizeDetails__e5sUw"><div class="react-code-size-details-banner CodeSizeDetails-module__Box__VcD6l"><div class="text-mono CodeSizeDetails-module__Box_1__GVxQL"><div data-testid="blob-size" class="CodeSizeDetails-module__Truncate_1__lE93V prc-Truncate-Truncate-2G1eo" data-inline="true" title="24.5 KB" style="--truncate-max-width: 100%;"><span>987 lines (842 loc) · 24.5 KB</span></div></div></div><div class="react-code-size-details-banner"><button data-component="Button" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-label="Code 55% faster with GitHub Copilot" class="prc-Button-ButtonBase-9n-Xk CopilotPopover-module__copilotButton__Ruc0t" data-loading="false" data-size="small" data-variant="invisible" id="_r_p0_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span></span></button></div></div><div class="react-blob-view-header-sticky BlobViewContent-module__stickyHeader__VwxB5" id="repos-sticky-header"><div class="BlobViewHeader-module__Box__yhm9u"><div class="react-blob-sticky-header"><div class="FileNameStickyHeader-module__outerWrapper__ZL4Xc FileNameStickyHeader-module__outerWrapperVisible__eXVyN FileNameStickyHeader-module__outerWrapperStickied__XqSue"><div class="FileNameStickyHeader-module__Box_5__dmNXA"><div class="Breadcrumb-module__container__Vxvev Breadcrumb-module__md__Wb1Gs"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Breadcrumb-module__nav__rQFDj"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Breadcrumb-module__list__ZH6zr"><li class="Breadcrumb-module__listItem__Ib0x_"><a class="Breadcrumb-module__repoLink__O2Nbs prc-Link-Link-9ZwDx" data-component="Link" data-testid="breadcrumbs-repo-link" href="https://github.com/s6ptember/fastapi-shop/tree/master" data-discover="true">fastapi-shop</a></li><li class="Breadcrumb-module__listItem__Ib0x_"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__md__Wb1Gs" aria-hidden="true">/</span><a class="Breadcrumb-module__directoryLink__kQy_t prc-Link-Link-9ZwDx" data-component="Link" href="https://github.com/s6ptember/fastapi-shop/tree/master/backend" data-discover="true">backend</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Breadcrumb-module__filename__equZR"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__md__Wb1Gs" aria-hidden="true">/</span><h1 class="Breadcrumb-module__filenameHeading__MNMtw Breadcrumb-module__md__Wb1Gs prc-Heading-Heading-MtWFE" tabindex="-1" id="sticky-file-name-id">test_commands.md</h1></div></div><button data-component="Button" type="button" class="prc-Button-ButtonBase-9n-Xk FileNameStickyHeader-module__Button__LSEU_ FileNameStickyHeader-module__GoToTopButton__nxAFn" data-loading="false" data-size="small" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Top</span></span></button></div></div></div><div class="BlobViewHeader-module__Box_1__VEmuQ BlobViewHeader-module__Box_1_stickied__L3NvW"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">File metadata and controls</h2><div class="BlobViewHeader-module__Box_2__icUs2"><ul aria-label="File view" class="prc-SegmentedControl-SegmentedControl-lqIXp BlobTabButtons-module__SegmentedControl__jen2u" data-variant="default" data-size="small"><li class="prc-SegmentedControl-Item-tSCQh" data-selected=""><button aria-current="true" class="prc-SegmentedControl-Button-E48xz" type="button" style="--separator-color: transparent;"><span class="prc-SegmentedControl-Content-1COlk segmentedControl-content"><div class="prc-SegmentedControl-Text-7S2y2 segmentedControl-text" data-text="Preview">Preview</div></span></button></li><li class="prc-SegmentedControl-Item-tSCQh"><button aria-current="false" class="prc-SegmentedControl-Button-E48xz" type="button" style="--separator-color: var(--borderColor-default);"><span class="prc-SegmentedControl-Content-1COlk segmentedControl-content"><div class="prc-SegmentedControl-Text-7S2y2 segmentedControl-text" data-text="Code">Code</div></span></button></li><li class="prc-SegmentedControl-Item-tSCQh"><button aria-current="false" class="prc-SegmentedControl-Button-E48xz" type="button" style="--separator-color: var(--borderColor-default);"><span class="prc-SegmentedControl-Content-1COlk segmentedControl-content"><div class="prc-SegmentedControl-Text-7S2y2 segmentedControl-text" data-text="Blame">Blame</div></span></button></li></ul><div class="d-none"></div><div class="react-code-size-details-in-header CodeSizeDetails-module__Box__VcD6l"><div class="text-mono CodeSizeDetails-module__Box_1__GVxQL"><div data-testid="blob-size" class="CodeSizeDetails-module__Truncate_1__lE93V prc-Truncate-Truncate-2G1eo" data-inline="true" title="24.5 KB" style="--truncate-max-width: 100%;"><span>987 lines (842 loc) · 24.5 KB</span></div></div></div><div class="react-code-size-details-in-header"><button data-component="Button" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-label="Code 55% faster with GitHub Copilot" class="prc-Button-ButtonBase-9n-Xk CopilotPopover-module__copilotButton__Ruc0t" data-loading="false" data-size="small" data-variant="invisible" id="_r_p5_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span></span></button></div></div><div class="BlobViewHeader-module__Box_3__ng6v2"><div class="d-none"></div><div class="react-blob-header-edit-and-raw-actions BlobViewHeader-module__Box_4__J4Y4W"><div class="d-none"></div><div class="prc-ButtonGroup-ButtonGroup-vFUrY"><div><a data-component="LinkButton" href="https://github.com/s6ptember/fastapi-shop/raw/refs/heads/master/backend/test_commands.md" data-testid="raw-button" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov BlobViewHeader-module__LinkButton__X9kx2" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Raw</span></span></a></div><div><button data-component="IconButton" type="button" data-testid="copy-raw-button" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_r_pb_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" data-component="Tooltip" aria-hidden="true" id="_r_pb_" popover="auto">Copy raw file</span></div><div><button data-component="IconButton" type="button" data-testid="download-raw-button" class="prc-Button-ButtonBase-9n-Xk BlobViewHeader-module__downloadButton__ef459 prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_r_pd_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" data-component="Tooltip" aria-hidden="true" id="_r_pd_" popover="auto">Download raw file</span></div></div><div class="d-none"></div><div class="prc-ButtonGroup-ButtonGroup-vFUrY"><div><a data-component="IconButton" type="button" data-testid="edit-button" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_r_pg_" href="https://github.com/s6ptember/fastapi-shop/edit/master/backend/test_commands.md" data-discover="true"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" data-component="Tooltip" aria-hidden="true" id="_r_pg_" popover="auto">Fork this repository and edit the file</span></div><div><button data-component="IconButton" type="button" data-testid="more-edit-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_r_pl_" id="_r_pi_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" data-component="Tooltip" aria-hidden="true" id="_r_pl_" popover="auto">More edit options</span></div></div></div><button data-component="IconButton" type="button" aria-pressed="false" class="prc-Button-ButtonBase-9n-Xk tmp-mr-2 TableOfContents-module__IconButton__jrlNM prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_r_pn_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-list-unordered" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" data-component="Tooltip" aria-hidden="true" id="_r_pn_" popover="auto">Outline</span><div class="react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" title="More file actions" data-testid="more-file-actions-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk js-blob-dropdown-click BlobViewHeader-module__IconButton__XrMQY prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_r_ps_" id="_r_pp_"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" data-component="Tooltip" aria-hidden="true" id="_r_ps_" popover="auto">Edit and raw actions</span></div></div></div></div><div></div></div><div class="BlobViewContent-module__blobContentWrapper__JS0W6"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="BlobContent-module__blobContentSection__VOgZq BlobContent-module__blobContentSectionMarkdown__mPLOK" style="margin-top: 46px;"><div class="js-snippet-clipboard-copy-unpositioned BlobContent-module__markdownBlob__T8jpG" data-hpc="true"><article class="markdown-body entry-content container-lg" itemprop="text"><div class="markdown-heading" dir="auto"><h1 tabindex="-1" class="heading-element" dir="auto">Руководство по тестированию API в Postman</h1><a id="user-content-руководство-по-тестированию-api-в-postman" class="anchor" aria-label="Permalink: Руководство по тестированию API в Postman" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D0%BE-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E-api-%D0%B2-postman"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Содержание</h2><a id="user-content-содержание" class="anchor" aria-label="Permalink: Содержание" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D1%81%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D0%B8%D0%B5"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li><a href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D0%BF%D0%BE%D0%B4%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BA%D0%B0">Подготовка</a></li>
<li><a href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F">Настройка окружения</a></li>
<li><a href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%8D%D0%BD%D0%B4%D0%BF%D0%BE%D0%B8%D0%BD%D1%82%D0%BE%D0%B2">Тестирование эндпоинтов</a></li>
<li><a href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-%D1%82%D0%B5%D1%81%D1%82%D1%8B">Автоматизированные тесты</a></li>
</ol>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Подготовка</h2><a id="user-content-подготовка" class="anchor" aria-label="Permalink: Подготовка" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D0%BF%D0%BE%D0%B4%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BA%D0%B0"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Запуск бэкенда</h3><a id="user-content-запуск-бэкенда" class="anchor" aria-label="Permalink: Запуск бэкенда" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA-%D0%B1%D1%8D%D0%BA%D0%B5%D0%BD%D0%B4%D0%B0"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c"><span class="pl-c">#</span> Установка зависимостей</span>
<span class="pl-c1">cd</span> backend
pip install -r requirements.txt

<span class="pl-c"><span class="pl-c">#</span> Заполнение базы данных тестовыми данными</span>
python seed_data.py

<span class="pl-c"><span class="pl-c">#</span> Запуск сервера</span>
python run.py</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="# Установка зависимостей
cd backend
pip install -r requirements.txt

# Заполнение базы данных тестовыми данными
python seed_data.py

# Запуск сервера
python run.py" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto">Сервер будет доступен по адресу: <code>http://localhost:8000</code></p>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Импорт коллекции в Postman</h3><a id="user-content-импорт-коллекции-в-postman" class="anchor" aria-label="Permalink: Импорт коллекции в Postman" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D0%B8%D0%BC%D0%BF%D0%BE%D1%80%D1%82-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8-%D0%B2-postman"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li>Откройте Postman</li>
<li>Нажмите <strong>Import</strong> → <strong>Raw text</strong></li>
<li>Скопируйте JSON коллекцию из раздела ниже</li>
</ol>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Настройка окружения</h2><a id="user-content-настройка-окружения" class="anchor" aria-label="Permalink: Настройка окружения" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Создайте новое окружение (Environment) в Postman:</p>
<p dir="auto"><strong>Имя:</strong> <code>FastAPI Shop Local</code></p>
<p dir="auto"><strong>Переменные:</strong></p>
<markdown-accessiblity-table data-catalyst=""><table>
<thead>
<tr>
<th>Variable</th>
<th>Initial Value</th>
<th>Current Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>base_url</code></td>
<td><code>http://localhost:8000</code></td>
<td><code>http://localhost:8000</code></td>
</tr>
<tr>
<td><code>product_id</code></td>
<td><code>1</code></td>
<td><code>1</code></td>
</tr>
<tr>
<td><code>category_id</code></td>
<td><code>1</code></td>
<td><code>1</code></td>
</tr>
</tbody>
</table></markdown-accessiblity-table>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Тестирование эндпоинтов</h2><a id="user-content-тестирование-эндпоинтов" class="anchor" aria-label="Permalink: Тестирование эндпоинтов" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%8D%D0%BD%D0%B4%D0%BF%D0%BE%D0%B8%D0%BD%D1%82%D0%BE%D0%B2"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">1. Health Check</h3><a id="user-content-1-health-check" class="anchor" aria-label="Permalink: 1. Health Check" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#1-health-check"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong>Проверка работоспособности сервера</strong></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>GET {{base_url}}/health
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="GET {{base_url}}/health" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (200 OK):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"status"</span>: <span class="pl-s"><span class="pl-pds">"</span>healthy<span class="pl-pds">"</span></span>
}
</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;status&quot;: &quot;healthy&quot;
}
" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Tests для добавления:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status code is 200"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">status</span><span class="pl-kos">(</span><span class="pl-c1">200</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status is healthy"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">status</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-en">eql</span><span class="pl-kos">(</span><span class="pl-s">"healthy"</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pm.test(&quot;Status code is 200&quot;, function () {
    pm.response.to.have.status(200);
});

pm.test(&quot;Status is healthy&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.status).to.eql(&quot;healthy&quot;);
});" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">2. Категории (Categories)</h3><a id="user-content-2-категории-categories" class="anchor" aria-label="Permalink: 2. Категории (Categories)" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#2-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8-categories"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">2.1. Получить все категории</h4><a id="user-content-21-получить-все-категории" class="anchor" aria-label="Permalink: 2.1. Получить все категории" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#21-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%B2%D1%81%D0%B5-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>GET {{base_url}}/api/categories
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="GET {{base_url}}/api/categories" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (200 OK):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>[
  {
    <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Electronics<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"slug"</span>: <span class="pl-s"><span class="pl-pds">"</span>electronics<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"id"</span>: <span class="pl-c1">1</span>
  },
  {
    <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Clothing<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"slug"</span>: <span class="pl-s"><span class="pl-pds">"</span>clothing<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"id"</span>: <span class="pl-c1">2</span>
  }
]</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="[
  {
    &quot;name&quot;: &quot;Electronics&quot;,
    &quot;slug&quot;: &quot;electronics&quot;,
    &quot;id&quot;: 1
  },
  {
    &quot;name&quot;: &quot;Clothing&quot;,
    &quot;slug&quot;: &quot;clothing&quot;,
    &quot;id&quot;: 2
  }
]" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Tests:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status code is 200"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">status</span><span class="pl-kos">(</span><span class="pl-c1">200</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Response is array"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">be</span><span class="pl-kos">.</span><span class="pl-en">an</span><span class="pl-kos">(</span><span class="pl-s">'array'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Categories have required fields"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">[</span><span class="pl-c1">0</span><span class="pl-kos">]</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'id'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">[</span><span class="pl-c1">0</span><span class="pl-kos">]</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'name'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">[</span><span class="pl-c1">0</span><span class="pl-kos">]</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'slug'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-c">// Сохраняем ID первой категории для других запросов</span>
<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">length</span> <span class="pl-c1">&gt;</span> <span class="pl-c1">0</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">environment</span><span class="pl-kos">.</span><span class="pl-en">set</span><span class="pl-kos">(</span><span class="pl-s">"category_id"</span><span class="pl-kos">,</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">[</span><span class="pl-c1">0</span><span class="pl-kos">]</span><span class="pl-kos">.</span><span class="pl-c1">id</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pm.test(&quot;Status code is 200&quot;, function () {
    pm.response.to.have.status(200);
});

pm.test(&quot;Response is array&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an(&#39;array&#39;);
});

pm.test(&quot;Categories have required fields&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData[0]).to.have.property(&#39;id&#39;);
    pm.expect(jsonData[0]).to.have.property(&#39;name&#39;);
    pm.expect(jsonData[0]).to.have.property(&#39;slug&#39;);
});

// Сохраняем ID первой категории для других запросов
if (pm.response.json().length &gt; 0) {
    pm.environment.set(&quot;category_id&quot;, pm.response.json()[0].id);
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">2.2. Получить категорию по ID</h4><a id="user-content-22-получить-категорию-по-id" class="anchor" aria-label="Permalink: 2.2. Получить категорию по ID" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#22-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8E-%D0%BF%D0%BE-id"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>GET {{base_url}}/api/categories/{{category_id}}
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="GET {{base_url}}/api/categories/{{category_id}}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (200 OK):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Electronics<span class="pl-pds">"</span></span>,
  <span class="pl-ent">"slug"</span>: <span class="pl-s"><span class="pl-pds">"</span>electronics<span class="pl-pds">"</span></span>,
  <span class="pl-ent">"id"</span>: <span class="pl-c1">1</span>
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;name&quot;: &quot;Electronics&quot;,
  &quot;slug&quot;: &quot;electronics&quot;,
  &quot;id&quot;: 1
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Tests:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status code is 200"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">status</span><span class="pl-kos">(</span><span class="pl-c1">200</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Category has correct structure"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'id'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'name'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'slug'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pm.test(&quot;Status code is 200&quot;, function () {
    pm.response.to.have.status(200);
});

pm.test(&quot;Category has correct structure&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property(&#39;id&#39;);
    pm.expect(jsonData).to.have.property(&#39;name&#39;);
    pm.expect(jsonData).to.have.property(&#39;slug&#39;);
});" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">2.3. Получить несуществующую категорию</h4><a id="user-content-23-получить-несуществующую-категорию" class="anchor" aria-label="Permalink: 2.3. Получить несуществующую категорию" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#23-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%BD%D0%B5%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D1%83%D1%8E-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8E"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>GET {{base_url}}/api/categories/9999
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="GET {{base_url}}/api/categories/9999" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (404 Not Found):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"detail"</span>: <span class="pl-s"><span class="pl-pds">"</span>Category with id 9999 not found<span class="pl-pds">"</span></span>
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;detail&quot;: &quot;Category with id 9999 not found&quot;
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Tests:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status code is 404"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">status</span><span class="pl-kos">(</span><span class="pl-c1">404</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Error message is correct"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">detail</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-en">include</span><span class="pl-kos">(</span><span class="pl-s">"not found"</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pm.test(&quot;Status code is 404&quot;, function () {
    pm.response.to.have.status(404);
});

pm.test(&quot;Error message is correct&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.detail).to.include(&quot;not found&quot;);
});" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">3. Товары (Products)</h3><a id="user-content-3-товары-products" class="anchor" aria-label="Permalink: 3. Товары (Products)" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#3-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%8B-products"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">3.1. Получить все товары</h4><a id="user-content-31-получить-все-товары" class="anchor" aria-label="Permalink: 3.1. Получить все товары" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#31-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%B2%D1%81%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%8B"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>GET {{base_url}}/api/products
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="GET {{base_url}}/api/products" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (200 OK):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"products"</span>: [
    {
      <span class="pl-ent">"id"</span>: <span class="pl-c1">1</span>,
      <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Wireless Headphones<span class="pl-pds">"</span></span>,
      <span class="pl-ent">"description"</span>: <span class="pl-s"><span class="pl-pds">"</span>High-quality wireless headphones...<span class="pl-pds">"</span></span>,
      <span class="pl-ent">"price"</span>: <span class="pl-c1">299.99</span>,
      <span class="pl-ent">"category_id"</span>: <span class="pl-c1">1</span>,
      <span class="pl-ent">"image_url"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://images.unsplash.com/...<span class="pl-pds">"</span></span>,
      <span class="pl-ent">"created_at"</span>: <span class="pl-s"><span class="pl-pds">"</span>2025-01-15T10:30:00<span class="pl-pds">"</span></span>,
      <span class="pl-ent">"category"</span>: {
        <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Electronics<span class="pl-pds">"</span></span>,
        <span class="pl-ent">"slug"</span>: <span class="pl-s"><span class="pl-pds">"</span>electronics<span class="pl-pds">"</span></span>,
        <span class="pl-ent">"id"</span>: <span class="pl-c1">1</span>
      }
    }
  ],
  <span class="pl-ent">"total"</span>: <span class="pl-c1">13</span>
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;products&quot;: [
    {
      &quot;id&quot;: 1,
      &quot;name&quot;: &quot;Wireless Headphones&quot;,
      &quot;description&quot;: &quot;High-quality wireless headphones...&quot;,
      &quot;price&quot;: 299.99,
      &quot;category_id&quot;: 1,
      &quot;image_url&quot;: &quot;https://images.unsplash.com/...&quot;,
      &quot;created_at&quot;: &quot;2025-01-15T10:30:00&quot;,
      &quot;category&quot;: {
        &quot;name&quot;: &quot;Electronics&quot;,
        &quot;slug&quot;: &quot;electronics&quot;,
        &quot;id&quot;: 1
      }
    }
  ],
  &quot;total&quot;: 13
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Tests:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status code is 200"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">status</span><span class="pl-kos">(</span><span class="pl-c1">200</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Response has products and total"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'products'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'total'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Products is an array"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">products</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">be</span><span class="pl-kos">.</span><span class="pl-en">an</span><span class="pl-kos">(</span><span class="pl-s">'array'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Product has complete structure"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">products</span><span class="pl-kos">.</span><span class="pl-c1">length</span> <span class="pl-c1">&gt;</span> <span class="pl-c1">0</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
        <span class="pl-k">var</span> <span class="pl-s1">product</span> <span class="pl-c1">=</span> <span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">products</span><span class="pl-kos">[</span><span class="pl-c1">0</span><span class="pl-kos">]</span><span class="pl-kos">;</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">product</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'id'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">product</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'name'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">product</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'price'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">product</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'category'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">product</span><span class="pl-kos">.</span><span class="pl-c1">category</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'id'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">product</span><span class="pl-kos">.</span><span class="pl-c1">category</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'name'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-kos">}</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-c">// Сохраняем ID первого товара</span>
<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">products</span><span class="pl-kos">.</span><span class="pl-c1">length</span> <span class="pl-c1">&gt;</span> <span class="pl-c1">0</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">environment</span><span class="pl-kos">.</span><span class="pl-en">set</span><span class="pl-kos">(</span><span class="pl-s">"product_id"</span><span class="pl-kos">,</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">products</span><span class="pl-kos">[</span><span class="pl-c1">0</span><span class="pl-kos">]</span><span class="pl-kos">.</span><span class="pl-c1">id</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pm.test(&quot;Status code is 200&quot;, function () {
    pm.response.to.have.status(200);
});

pm.test(&quot;Response has products and total&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property(&#39;products&#39;);
    pm.expect(jsonData).to.have.property(&#39;total&#39;);
});

pm.test(&quot;Products is an array&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.products).to.be.an(&#39;array&#39;);
});

pm.test(&quot;Product has complete structure&quot;, function () {
    var jsonData = pm.response.json();
    if (jsonData.products.length &gt; 0) {
        var product = jsonData.products[0];
        pm.expect(product).to.have.property(&#39;id&#39;);
        pm.expect(product).to.have.property(&#39;name&#39;);
        pm.expect(product).to.have.property(&#39;price&#39;);
        pm.expect(product).to.have.property(&#39;category&#39;);
        pm.expect(product.category).to.have.property(&#39;id&#39;);
        pm.expect(product.category).to.have.property(&#39;name&#39;);
    }
});

// Сохраняем ID первого товара
if (pm.response.json().products.length &gt; 0) {
    pm.environment.set(&quot;product_id&quot;, pm.response.json().products[0].id);
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">3.2. Получить товар по ID</h4><a id="user-content-32-получить-товар-по-id" class="anchor" aria-label="Permalink: 3.2. Получить товар по ID" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#32-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D0%B2%D0%B0%D1%80-%D0%BF%D0%BE-id"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>GET {{base_url}}/api/products/{{product_id}}
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="GET {{base_url}}/api/products/{{product_id}}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Tests:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status code is 200"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">status</span><span class="pl-kos">(</span><span class="pl-c1">200</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Product has all required fields"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'id'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'name'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'price'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'category_id'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'category'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Price is positive number"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">price</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">be</span><span class="pl-kos">.</span><span class="pl-en">above</span><span class="pl-kos">(</span><span class="pl-c1">0</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pm.test(&quot;Status code is 200&quot;, function () {
    pm.response.to.have.status(200);
});

pm.test(&quot;Product has all required fields&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property(&#39;id&#39;);
    pm.expect(jsonData).to.have.property(&#39;name&#39;);
    pm.expect(jsonData).to.have.property(&#39;price&#39;);
    pm.expect(jsonData).to.have.property(&#39;category_id&#39;);
    pm.expect(jsonData).to.have.property(&#39;category&#39;);
});

pm.test(&quot;Price is positive number&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.price).to.be.above(0);
});" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">3.3. Получить товары по категории</h4><a id="user-content-33-получить-товары-по-категории" class="anchor" aria-label="Permalink: 3.3. Получить товары по категории" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#33-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%8B-%D0%BF%D0%BE-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>GET {{base_url}}/api/products/category/{{category_id}}
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="GET {{base_url}}/api/products/category/{{category_id}}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Tests:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status code is 200"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">status</span><span class="pl-kos">(</span><span class="pl-c1">200</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"All products belong to specified category"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-k">var</span> <span class="pl-s1">categoryId</span> <span class="pl-c1">=</span> <span class="pl-en">parseInt</span><span class="pl-kos">(</span><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">environment</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">"category_id"</span><span class="pl-kos">)</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

    <span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">products</span><span class="pl-kos">.</span><span class="pl-en">forEach</span><span class="pl-kos">(</span><span class="pl-k">function</span><span class="pl-kos">(</span><span class="pl-s1">product</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">product</span><span class="pl-kos">.</span><span class="pl-c1">category_id</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-en">eql</span><span class="pl-kos">(</span><span class="pl-s1">categoryId</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pm.test(&quot;Status code is 200&quot;, function () {
    pm.response.to.have.status(200);
});

pm.test(&quot;All products belong to specified category&quot;, function () {
    var jsonData = pm.response.json();
    var categoryId = parseInt(pm.environment.get(&quot;category_id&quot;));

    jsonData.products.forEach(function(product) {
        pm.expect(product.category_id).to.eql(categoryId);
    });
});" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">3.4. Получить товары несуществующей категории</h4><a id="user-content-34-получить-товары-несуществующей-категории" class="anchor" aria-label="Permalink: 3.4. Получить товары несуществующей категории" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#34-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%8B-%D0%BD%D0%B5%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B5%D0%B9-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>GET {{base_url}}/api/products/category/9999
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="GET {{base_url}}/api/products/category/9999" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (404 Not Found):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"detail"</span>: <span class="pl-s"><span class="pl-pds">"</span>Category with id 9999 not found<span class="pl-pds">"</span></span>
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;detail&quot;: &quot;Category with id 9999 not found&quot;
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">4. Корзина (Cart)</h3><a id="user-content-4-корзина-cart" class="anchor" aria-label="Permalink: 4. Корзина (Cart)" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#4-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D0%B0-cart"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">4.1. Добавить товар в корзину</h4><a id="user-content-41-добавить-товар-в-корзину" class="anchor" aria-label="Permalink: 4.1. Добавить товар в корзину" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#41-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D0%B2%D0%B0%D1%80-%D0%B2-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D1%83"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>POST {{base_url}}/api/cart/add
Content-Type: application/json

{
  "product_id": 1,
  "quantity": 2,
  "cart": {}
}
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="POST {{base_url}}/api/cart/add
Content-Type: application/json

{
  &quot;product_id&quot;: 1,
  &quot;quantity&quot;: 2,
  &quot;cart&quot;: {}
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (200 OK):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"cart"</span>: {
    <span class="pl-ent">"1"</span>: <span class="pl-c1">2</span>
  }
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;cart&quot;: {
    &quot;1&quot;: 2
  }
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Tests:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status code is 200"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">status</span><span class="pl-kos">(</span><span class="pl-c1">200</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Cart contains added product"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">cart</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'1'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">cart</span><span class="pl-kos">[</span><span class="pl-s">'1'</span><span class="pl-kos">]</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-en">eql</span><span class="pl-kos">(</span><span class="pl-c1">2</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-c">// Сохраняем корзину для следующих запросов</span>
<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">environment</span><span class="pl-kos">.</span><span class="pl-en">set</span><span class="pl-kos">(</span><span class="pl-s">"cart"</span><span class="pl-kos">,</span> <span class="pl-c1">JSON</span><span class="pl-kos">.</span><span class="pl-en">stringify</span><span class="pl-kos">(</span><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">cart</span><span class="pl-kos">)</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pm.test(&quot;Status code is 200&quot;, function () {
    pm.response.to.have.status(200);
});

pm.test(&quot;Cart contains added product&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.cart).to.have.property(&#39;1&#39;);
    pm.expect(jsonData.cart[&#39;1&#39;]).to.eql(2);
});

// Сохраняем корзину для следующих запросов
pm.environment.set(&quot;cart&quot;, JSON.stringify(pm.response.json().cart));" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">4.2. Добавить ещё один товар</h4><a id="user-content-42-добавить-ещё-один-товар" class="anchor" aria-label="Permalink: 4.2. Добавить ещё один товар" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#42-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B5%D1%89%D1%91-%D0%BE%D0%B4%D0%B8%D0%BD-%D1%82%D0%BE%D0%B2%D0%B0%D1%80"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>POST {{base_url}}/api/cart/add
Content-Type: application/json

{
  "product_id": 2,
  "quantity": 1,
  "cart": {{cart}}
}
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="POST {{base_url}}/api/cart/add
Content-Type: application/json

{
  &quot;product_id&quot;: 2,
  &quot;quantity&quot;: 1,
  &quot;cart&quot;: {{cart}}
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Pre-request Script:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c">// Загружаем корзину из переменной окружения</span>
<span class="pl-k">var</span> <span class="pl-s1">cart</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">environment</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">"cart"</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">cart</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">variables</span><span class="pl-kos">.</span><span class="pl-en">set</span><span class="pl-kos">(</span><span class="pl-s">"cart"</span><span class="pl-kos">,</span> <span class="pl-s1">cart</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span> <span class="pl-k">else</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">variables</span><span class="pl-kos">.</span><span class="pl-en">set</span><span class="pl-kos">(</span><span class="pl-s">"cart"</span><span class="pl-kos">,</span> <span class="pl-s">"{}"</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="// Загружаем корзину из переменной окружения
var cart = pm.environment.get(&quot;cart&quot;);
if (cart) {
    pm.variables.set(&quot;cart&quot;, cart);
} else {
    pm.variables.set(&quot;cart&quot;, &quot;{}&quot;);
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">4.3. Получить детали корзины</h4><a id="user-content-43-получить-детали-корзины" class="anchor" aria-label="Permalink: 4.3. Получить детали корзины" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#43-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%B4%D0%B5%D1%82%D0%B0%D0%BB%D0%B8-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D1%8B"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>POST {{base_url}}/api/cart
Content-Type: application/json

{
  "1": 2,
  "2": 1
}
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="POST {{base_url}}/api/cart
Content-Type: application/json

{
  &quot;1&quot;: 2,
  &quot;2&quot;: 1
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (200 OK):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"items"</span>: [
    {
      <span class="pl-ent">"product_id"</span>: <span class="pl-c1">1</span>,
      <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Wireless Headphones<span class="pl-pds">"</span></span>,
      <span class="pl-ent">"price"</span>: <span class="pl-c1">299.99</span>,
      <span class="pl-ent">"quantity"</span>: <span class="pl-c1">2</span>,
      <span class="pl-ent">"subtotal"</span>: <span class="pl-c1">600.0</span>,
      <span class="pl-ent">"image_url"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://images.unsplash.com/...<span class="pl-pds">"</span></span>
    },
    {
      <span class="pl-ent">"product_id"</span>: <span class="pl-c1">2</span>,
      <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Smart Watch Pro<span class="pl-pds">"</span></span>,
      <span class="pl-ent">"price"</span>: <span class="pl-c1">399.99</span>,
      <span class="pl-ent">"quantity"</span>: <span class="pl-c1">1</span>,
      <span class="pl-ent">"subtotal"</span>: <span class="pl-c1">400.0</span>,
      <span class="pl-ent">"image_url"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://images.unsplash.com/...<span class="pl-pds">"</span></span>
    }
  ],
  <span class="pl-ent">"total"</span>: <span class="pl-c1">1000.0</span>,
  <span class="pl-ent">"items_count"</span>: <span class="pl-c1">3</span>
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;items&quot;: [
    {
      &quot;product_id&quot;: 1,
      &quot;name&quot;: &quot;Wireless Headphones&quot;,
      &quot;price&quot;: 299.99,
      &quot;quantity&quot;: 2,
      &quot;subtotal&quot;: 600.0,
      &quot;image_url&quot;: &quot;https://images.unsplash.com/...&quot;
    },
    {
      &quot;product_id&quot;: 2,
      &quot;name&quot;: &quot;Smart Watch Pro&quot;,
      &quot;price&quot;: 399.99,
      &quot;quantity&quot;: 1,
      &quot;subtotal&quot;: 400.0,
      &quot;image_url&quot;: &quot;https://images.unsplash.com/...&quot;
    }
  ],
  &quot;total&quot;: 1000.0,
  &quot;items_count&quot;: 3
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Tests:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status code is 200"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">status</span><span class="pl-kos">(</span><span class="pl-c1">200</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Cart has all required fields"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'items'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'total'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'items_count'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Items have correct structure"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">items</span><span class="pl-kos">.</span><span class="pl-c1">length</span> <span class="pl-c1">&gt;</span> <span class="pl-c1">0</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
        <span class="pl-k">var</span> <span class="pl-s1">item</span> <span class="pl-c1">=</span> <span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">items</span><span class="pl-kos">[</span><span class="pl-c1">0</span><span class="pl-kos">]</span><span class="pl-kos">;</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">item</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'product_id'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">item</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'name'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">item</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'price'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">item</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'quantity'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
        <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">item</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'subtotal'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-kos">}</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Total is calculated correctly"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-k">var</span> <span class="pl-s1">calculatedTotal</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span><span class="pl-kos">;</span>

    <span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">items</span><span class="pl-kos">.</span><span class="pl-en">forEach</span><span class="pl-kos">(</span><span class="pl-k">function</span><span class="pl-kos">(</span><span class="pl-s1">item</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
        <span class="pl-s1">calculatedTotal</span> <span class="pl-c1">+=</span> <span class="pl-s1">item</span><span class="pl-kos">.</span><span class="pl-c1">subtotal</span><span class="pl-kos">;</span>
    <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">total</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-en">eql</span><span class="pl-kos">(</span><span class="pl-s1">calculatedTotal</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Items count is correct"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-k">var</span> <span class="pl-s1">totalQuantity</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span><span class="pl-kos">;</span>

    <span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">items</span><span class="pl-kos">.</span><span class="pl-en">forEach</span><span class="pl-kos">(</span><span class="pl-k">function</span><span class="pl-kos">(</span><span class="pl-s1">item</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
        <span class="pl-s1">totalQuantity</span> <span class="pl-c1">+=</span> <span class="pl-s1">item</span><span class="pl-kos">.</span><span class="pl-c1">quantity</span><span class="pl-kos">;</span>
    <span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">items_count</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-en">eql</span><span class="pl-kos">(</span><span class="pl-s1">totalQuantity</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pm.test(&quot;Status code is 200&quot;, function () {
    pm.response.to.have.status(200);
});

pm.test(&quot;Cart has all required fields&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property(&#39;items&#39;);
    pm.expect(jsonData).to.have.property(&#39;total&#39;);
    pm.expect(jsonData).to.have.property(&#39;items_count&#39;);
});

pm.test(&quot;Items have correct structure&quot;, function () {
    var jsonData = pm.response.json();
    if (jsonData.items.length &gt; 0) {
        var item = jsonData.items[0];
        pm.expect(item).to.have.property(&#39;product_id&#39;);
        pm.expect(item).to.have.property(&#39;name&#39;);
        pm.expect(item).to.have.property(&#39;price&#39;);
        pm.expect(item).to.have.property(&#39;quantity&#39;);
        pm.expect(item).to.have.property(&#39;subtotal&#39;);
    }
});

pm.test(&quot;Total is calculated correctly&quot;, function () {
    var jsonData = pm.response.json();
    var calculatedTotal = 0;

    jsonData.items.forEach(function(item) {
        calculatedTotal += item.subtotal;
    });

    pm.expect(jsonData.total).to.eql(calculatedTotal);
});

pm.test(&quot;Items count is correct&quot;, function () {
    var jsonData = pm.response.json();
    var totalQuantity = 0;

    jsonData.items.forEach(function(item) {
        totalQuantity += item.quantity;
    });

    pm.expect(jsonData.items_count).to.eql(totalQuantity);
});" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">4.4. Обновить количество товара</h4><a id="user-content-44-обновить-количество-товара" class="anchor" aria-label="Permalink: 4.4. Обновить количество товара" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#44-%D0%BE%D0%B1%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>PUT {{base_url}}/api/cart/update
Content-Type: application/json

{
  "product_id": 1,
  "quantity": 5,
  "cart": {
    "1": 2,
    "2": 1
  }
}
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="PUT {{base_url}}/api/cart/update
Content-Type: application/json

{
  &quot;product_id&quot;: 1,
  &quot;quantity&quot;: 5,
  &quot;cart&quot;: {
    &quot;1&quot;: 2,
    &quot;2&quot;: 1
  }
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (200 OK):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"cart"</span>: {
    <span class="pl-ent">"1"</span>: <span class="pl-c1">5</span>,
    <span class="pl-ent">"2"</span>: <span class="pl-c1">1</span>
  }
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;cart&quot;: {
    &quot;1&quot;: 5,
    &quot;2&quot;: 1
  }
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Tests:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status code is 200"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">status</span><span class="pl-kos">(</span><span class="pl-c1">200</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Quantity was updated"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">cart</span><span class="pl-kos">[</span><span class="pl-s">'1'</span><span class="pl-kos">]</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-en">eql</span><span class="pl-kos">(</span><span class="pl-c1">5</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pm.test(&quot;Status code is 200&quot;, function () {
    pm.response.to.have.status(200);
});

pm.test(&quot;Quantity was updated&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.cart[&#39;1&#39;]).to.eql(5);
});" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">4.5. Удалить товар из корзины</h4><a id="user-content-45-удалить-товар-из-корзины" class="anchor" aria-label="Permalink: 4.5. Удалить товар из корзины" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#45-%D1%83%D0%B4%D0%B0%D0%BB%D0%B8%D1%82%D1%8C-%D1%82%D0%BE%D0%B2%D0%B0%D1%80-%D0%B8%D0%B7-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D1%8B"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>DELETE {{base_url}}/api/cart/remove/1
Content-Type: application/json

{
  "cart": {
    "1": 5,
    "2": 1
  }
}
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="DELETE {{base_url}}/api/cart/remove/1
Content-Type: application/json

{
  &quot;cart&quot;: {
    &quot;1&quot;: 5,
    &quot;2&quot;: 1
  }
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (200 OK):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"cart"</span>: {
    <span class="pl-ent">"2"</span>: <span class="pl-c1">1</span>
  }
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;cart&quot;: {
    &quot;2&quot;: 1
  }
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Tests:</strong></p>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Status code is 200"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">status</span><span class="pl-kos">(</span><span class="pl-c1">200</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Product was removed from cart"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-k">var</span> <span class="pl-s1">jsonData</span> <span class="pl-c1">=</span> <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-en">json</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">jsonData</span><span class="pl-kos">.</span><span class="pl-c1">cart</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">not</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">property</span><span class="pl-kos">(</span><span class="pl-s">'1'</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="pm.test(&quot;Status code is 200&quot;, function () {
    pm.response.to.have.status(200);
});

pm.test(&quot;Product was removed from cart&quot;, function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.cart).to.not.have.property(&#39;1&#39;);
});" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">4.6. Получить пустую корзину</h4><a id="user-content-46-получить-пустую-корзину" class="anchor" aria-label="Permalink: 4.6. Получить пустую корзину" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#46-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%BF%D1%83%D1%81%D1%82%D1%83%D1%8E-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D1%83"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>POST {{base_url}}/api/cart
Content-Type: application/json

{}
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="POST {{base_url}}/api/cart
Content-Type: application/json

{}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (200 OK):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"items"</span>: [],
  <span class="pl-ent">"total"</span>: <span class="pl-c1">0.0</span>,
  <span class="pl-ent">"items_count"</span>: <span class="pl-c1">0</span>
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;items&quot;: [],
  &quot;total&quot;: 0.0,
  &quot;items_count&quot;: 0
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto">4.7. Добавить несуществующий товар</h4><a id="user-content-47-добавить-несуществующий-товар" class="anchor" aria-label="Permalink: 4.7. Добавить несуществующий товар" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#47-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BD%D0%B5%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B8%D0%B9-%D1%82%D0%BE%D0%B2%D0%B0%D1%80"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>POST {{base_url}}/api/cart/add
Content-Type: application/json

{
  "product_id": 9999,
  "quantity": 1,
  "cart": {}
}
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="POST {{base_url}}/api/cart/add
Content-Type: application/json

{
  &quot;product_id&quot;: 9999,
  &quot;quantity&quot;: 1,
  &quot;cart&quot;: {}
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><strong>Ожидаемый ответ (404 Not Found):</strong></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"detail"</span>: <span class="pl-s"><span class="pl-pds">"</span>Product with id 9999 not found<span class="pl-pds">"</span></span>
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;detail&quot;: &quot;Product with id 9999 not found&quot;
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Автоматизированные тесты</h2><a id="user-content-автоматизированные-тесты" class="anchor" aria-label="Permalink: Автоматизированные тесты" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-%D1%82%D0%B5%D1%81%D1%82%D1%8B"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Создание Test Suite</h3><a id="user-content-создание-test-suite" class="anchor" aria-label="Permalink: Создание Test Suite" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-test-suite"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Вы можете создать последовательность тестов в Postman Collection Runner:</p>
<ol dir="auto">
<li><strong>Setup Tests</strong> → Health Check</li>
<li><strong>Categories Tests</strong> → Get All, Get by ID, Get Invalid</li>
<li><strong>Products Tests</strong> → Get All, Get by ID, Get by Category</li>
<li><strong>Cart Tests</strong> → Add, Update, Remove, Get Details</li>
</ol>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Pre-request Script для всей коллекции</h3><a id="user-content-pre-request-script-для-всей-коллекции" class="anchor" aria-label="Permalink: Pre-request Script для всей коллекции" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#pre-request-script-%D0%B4%D0%BB%D1%8F-%D0%B2%D1%81%D0%B5%D0%B9-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c">// Устанавливаем базовые переменные, если их нет</span>
<span class="pl-k">if</span> <span class="pl-kos">(</span><span class="pl-c1">!</span><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">environment</span><span class="pl-kos">.</span><span class="pl-en">get</span><span class="pl-kos">(</span><span class="pl-s">"base_url"</span><span class="pl-kos">)</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">environment</span><span class="pl-kos">.</span><span class="pl-en">set</span><span class="pl-kos">(</span><span class="pl-s">"base_url"</span><span class="pl-kos">,</span> <span class="pl-s">"http://localhost:8000"</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span>

<span class="pl-c">// Добавляем timestamp для уникальных запросов</span>
<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">variables</span><span class="pl-kos">.</span><span class="pl-en">set</span><span class="pl-kos">(</span><span class="pl-s">"timestamp"</span><span class="pl-kos">,</span> <span class="pl-v">Date</span><span class="pl-kos">.</span><span class="pl-en">now</span><span class="pl-kos">(</span><span class="pl-kos">)</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="// Устанавливаем базовые переменные, если их нет
if (!pm.environment.get(&quot;base_url&quot;)) {
    pm.environment.set(&quot;base_url&quot;, &quot;http://localhost:8000&quot;);
}

// Добавляем timestamp для уникальных запросов
pm.variables.set(&quot;timestamp&quot;, Date.now());" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">Tests для всей коллекции</h3><a id="user-content-tests-для-всей-коллекции" class="anchor" aria-label="Permalink: Tests для всей коллекции" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#tests-%D0%B4%D0%BB%D1%8F-%D0%B2%D1%81%D0%B5%D0%B9-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="highlight highlight-source-js notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c">// Проверка времени ответа</span>
<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Response time is less than 500ms"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">expect</span><span class="pl-kos">(</span><span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">responseTime</span><span class="pl-kos">)</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">be</span><span class="pl-kos">.</span><span class="pl-en">below</span><span class="pl-kos">(</span><span class="pl-c1">500</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span>

<span class="pl-c">// Проверка наличия Content-Type</span>
<span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-en">test</span><span class="pl-kos">(</span><span class="pl-s">"Content-Type is present"</span><span class="pl-kos">,</span> <span class="pl-k">function</span> <span class="pl-kos">(</span><span class="pl-kos">)</span> <span class="pl-kos">{</span>
    <span class="pl-s1">pm</span><span class="pl-kos">.</span><span class="pl-c1">response</span><span class="pl-kos">.</span><span class="pl-c1">to</span><span class="pl-kos">.</span><span class="pl-c1">have</span><span class="pl-kos">.</span><span class="pl-en">header</span><span class="pl-kos">(</span><span class="pl-s">"Content-Type"</span><span class="pl-kos">)</span><span class="pl-kos">;</span>
<span class="pl-kos">}</span><span class="pl-kos">)</span><span class="pl-kos">;</span></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="// Проверка времени ответа
pm.test(&quot;Response time is less than 500ms&quot;, function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

// Проверка наличия Content-Type
pm.test(&quot;Content-Type is present&quot;, function () {
    pm.response.to.have.header(&quot;Content-Type&quot;);
});" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Коллекция Postman (JSON)</h2><a id="user-content-коллекция-postman-json" class="anchor" aria-label="Permalink: Коллекция Postman (JSON)" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D1%8F-postman-json"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">Сохраните этот JSON и импортируйте в Postman:</p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
  <span class="pl-ent">"info"</span>: {
    <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>FastAPI Shop API<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"description"</span>: <span class="pl-s"><span class="pl-pds">"</span>Коллекция для тестирования API интернет-магазина<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"schema"</span>: <span class="pl-s"><span class="pl-pds">"</span>https://schema.getpostman.com/json/collection/v2.1.0/collection.json<span class="pl-pds">"</span></span>
  },
  <span class="pl-ent">"item"</span>: [
    {
      <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Health<span class="pl-pds">"</span></span>,
      <span class="pl-ent">"item"</span>: [
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Health Check<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>GET<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [],
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/health<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>health<span class="pl-pds">"</span></span>]
            }
          },
          <span class="pl-ent">"event"</span>: [
            {
              <span class="pl-ent">"listen"</span>: <span class="pl-s"><span class="pl-pds">"</span>test<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"script"</span>: {
                <span class="pl-ent">"exec"</span>: [
                  <span class="pl-s"><span class="pl-pds">"</span>pm.test(<span class="pl-cce">\"</span>Status code is 200<span class="pl-cce">\"</span>, function () {<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>    pm.response.to.have.status(200);<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>});<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span><span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>pm.test(<span class="pl-cce">\"</span>Status is healthy<span class="pl-cce">\"</span>, function () {<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>    var jsonData = pm.response.json();<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>    pm.expect(jsonData.status).to.eql(<span class="pl-cce">\"</span>healthy<span class="pl-cce">\"</span>);<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>});<span class="pl-pds">"</span></span>
                ]
              }
            }
          ]
        }
      ]
    },
    {
      <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Categories<span class="pl-pds">"</span></span>,
      <span class="pl-ent">"item"</span>: [
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Get All Categories<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>GET<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [],
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/api/categories<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>api<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>categories<span class="pl-pds">"</span></span>]
            }
          },
          <span class="pl-ent">"event"</span>: [
            {
              <span class="pl-ent">"listen"</span>: <span class="pl-s"><span class="pl-pds">"</span>test<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"script"</span>: {
                <span class="pl-ent">"exec"</span>: [
                  <span class="pl-s"><span class="pl-pds">"</span>pm.test(<span class="pl-cce">\"</span>Status code is 200<span class="pl-cce">\"</span>, function () {<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>    pm.response.to.have.status(200);<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>});<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span><span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>pm.test(<span class="pl-cce">\"</span>Response is array<span class="pl-cce">\"</span>, function () {<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>    var jsonData = pm.response.json();<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>    pm.expect(jsonData).to.be.an('array');<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>});<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span><span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>if (pm.response.json().length &gt; 0) {<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>    pm.environment.set(<span class="pl-cce">\"</span>category_id<span class="pl-cce">\"</span>, pm.response.json()[0].id);<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>}<span class="pl-pds">"</span></span>
                ]
              }
            }
          ]
        },
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Get Category by ID<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>GET<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [],
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/api/categories/{{category_id}}<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>api<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>categories<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>{{category_id}}<span class="pl-pds">"</span></span>]
            }
          }
        },
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Get Invalid Category<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>GET<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [],
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/api/categories/9999<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>api<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>categories<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>9999<span class="pl-pds">"</span></span>]
            }
          },
          <span class="pl-ent">"event"</span>: [
            {
              <span class="pl-ent">"listen"</span>: <span class="pl-s"><span class="pl-pds">"</span>test<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"script"</span>: {
                <span class="pl-ent">"exec"</span>: [
                  <span class="pl-s"><span class="pl-pds">"</span>pm.test(<span class="pl-cce">\"</span>Status code is 404<span class="pl-cce">\"</span>, function () {<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>    pm.response.to.have.status(404);<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>});<span class="pl-pds">"</span></span>
                ]
              }
            }
          ]
        }
      ]
    },
    {
      <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Products<span class="pl-pds">"</span></span>,
      <span class="pl-ent">"item"</span>: [
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Get All Products<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>GET<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [],
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/api/products<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>api<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>products<span class="pl-pds">"</span></span>]
            }
          },
          <span class="pl-ent">"event"</span>: [
            {
              <span class="pl-ent">"listen"</span>: <span class="pl-s"><span class="pl-pds">"</span>test<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"script"</span>: {
                <span class="pl-ent">"exec"</span>: [
                  <span class="pl-s"><span class="pl-pds">"</span>pm.test(<span class="pl-cce">\"</span>Status code is 200<span class="pl-cce">\"</span>, function () {<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>    pm.response.to.have.status(200);<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>});<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span><span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>if (pm.response.json().products.length &gt; 0) {<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>    pm.environment.set(<span class="pl-cce">\"</span>product_id<span class="pl-cce">\"</span>, pm.response.json().products[0].id);<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>}<span class="pl-pds">"</span></span>
                ]
              }
            }
          ]
        },
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Get Product by ID<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>GET<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [],
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/api/products/{{product_id}}<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>api<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>products<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>{{product_id}}<span class="pl-pds">"</span></span>]
            }
          }
        },
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Get Products by Category<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>GET<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [],
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/api/products/category/{{category_id}}<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>api<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>products<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>category<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>{{category_id}}<span class="pl-pds">"</span></span>]
            }
          }
        }
      ]
    },
    {
      <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Cart<span class="pl-pds">"</span></span>,
      <span class="pl-ent">"item"</span>: [
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Add to Cart<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>POST<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [
              {
                <span class="pl-ent">"key"</span>: <span class="pl-s"><span class="pl-pds">"</span>Content-Type<span class="pl-pds">"</span></span>,
                <span class="pl-ent">"value"</span>: <span class="pl-s"><span class="pl-pds">"</span>application/json<span class="pl-pds">"</span></span>
              }
            ],
            <span class="pl-ent">"body"</span>: {
              <span class="pl-ent">"mode"</span>: <span class="pl-s"><span class="pl-pds">"</span>raw<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{<span class="pl-cce">\n</span>  <span class="pl-cce">\"</span>product_id<span class="pl-cce">\"</span>: 1,<span class="pl-cce">\n</span>  <span class="pl-cce">\"</span>quantity<span class="pl-cce">\"</span>: 2,<span class="pl-cce">\n</span>  <span class="pl-cce">\"</span>cart<span class="pl-cce">\"</span>: {}<span class="pl-cce">\n</span>}<span class="pl-pds">"</span></span>
            },
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/api/cart/add<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>api<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>cart<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>add<span class="pl-pds">"</span></span>]
            }
          },
          <span class="pl-ent">"event"</span>: [
            {
              <span class="pl-ent">"listen"</span>: <span class="pl-s"><span class="pl-pds">"</span>test<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"script"</span>: {
                <span class="pl-ent">"exec"</span>: [
                  <span class="pl-s"><span class="pl-pds">"</span>pm.test(<span class="pl-cce">\"</span>Status code is 200<span class="pl-cce">\"</span>, function () {<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>    pm.response.to.have.status(200);<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>});<span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span><span class="pl-pds">"</span></span>,
                  <span class="pl-s"><span class="pl-pds">"</span>pm.environment.set(<span class="pl-cce">\"</span>cart<span class="pl-cce">\"</span>, JSON.stringify(pm.response.json().cart));<span class="pl-pds">"</span></span>
                ]
              }
            }
          ]
        },
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Get Cart Details<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>POST<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [
              {
                <span class="pl-ent">"key"</span>: <span class="pl-s"><span class="pl-pds">"</span>Content-Type<span class="pl-pds">"</span></span>,
                <span class="pl-ent">"value"</span>: <span class="pl-s"><span class="pl-pds">"</span>application/json<span class="pl-pds">"</span></span>
              }
            ],
            <span class="pl-ent">"body"</span>: {
              <span class="pl-ent">"mode"</span>: <span class="pl-s"><span class="pl-pds">"</span>raw<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{<span class="pl-cce">\n</span>  <span class="pl-cce">\"</span>1<span class="pl-cce">\"</span>: 2,<span class="pl-cce">\n</span>  <span class="pl-cce">\"</span>2<span class="pl-cce">\"</span>: 1<span class="pl-cce">\n</span>}<span class="pl-pds">"</span></span>
            },
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/api/cart<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>api<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>cart<span class="pl-pds">"</span></span>]
            }
          }
        },
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Update Cart Item<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>PUT<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [
              {
                <span class="pl-ent">"key"</span>: <span class="pl-s"><span class="pl-pds">"</span>Content-Type<span class="pl-pds">"</span></span>,
                <span class="pl-ent">"value"</span>: <span class="pl-s"><span class="pl-pds">"</span>application/json<span class="pl-pds">"</span></span>
              }
            ],
            <span class="pl-ent">"body"</span>: {
              <span class="pl-ent">"mode"</span>: <span class="pl-s"><span class="pl-pds">"</span>raw<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{<span class="pl-cce">\n</span>  <span class="pl-cce">\"</span>product_id<span class="pl-cce">\"</span>: 1,<span class="pl-cce">\n</span>  <span class="pl-cce">\"</span>quantity<span class="pl-cce">\"</span>: 5,<span class="pl-cce">\n</span>  <span class="pl-cce">\"</span>cart<span class="pl-cce">\"</span>: {<span class="pl-cce">\n</span>    <span class="pl-cce">\"</span>1<span class="pl-cce">\"</span>: 2,<span class="pl-cce">\n</span>    <span class="pl-cce">\"</span>2<span class="pl-cce">\"</span>: 1<span class="pl-cce">\n</span>  }<span class="pl-cce">\n</span>}<span class="pl-pds">"</span></span>
            },
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/api/cart/update<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>api<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>cart<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>update<span class="pl-pds">"</span></span>]
            }
          }
        },
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Remove from Cart<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>DELETE<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [
              {
                <span class="pl-ent">"key"</span>: <span class="pl-s"><span class="pl-pds">"</span>Content-Type<span class="pl-pds">"</span></span>,
                <span class="pl-ent">"value"</span>: <span class="pl-s"><span class="pl-pds">"</span>application/json<span class="pl-pds">"</span></span>
              }
            ],
            <span class="pl-ent">"body"</span>: {
              <span class="pl-ent">"mode"</span>: <span class="pl-s"><span class="pl-pds">"</span>raw<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{<span class="pl-cce">\n</span>  <span class="pl-cce">\"</span>cart<span class="pl-cce">\"</span>: {<span class="pl-cce">\n</span>    <span class="pl-cce">\"</span>1<span class="pl-cce">\"</span>: 5,<span class="pl-cce">\n</span>    <span class="pl-cce">\"</span>2<span class="pl-cce">\"</span>: 1<span class="pl-cce">\n</span>  }<span class="pl-cce">\n</span>}<span class="pl-pds">"</span></span>
            },
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/api/cart/remove/1<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>api<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>cart<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>remove<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>1<span class="pl-pds">"</span></span>]
            }
          }
        },
        {
          <span class="pl-ent">"name"</span>: <span class="pl-s"><span class="pl-pds">"</span>Get Empty Cart<span class="pl-pds">"</span></span>,
          <span class="pl-ent">"request"</span>: {
            <span class="pl-ent">"method"</span>: <span class="pl-s"><span class="pl-pds">"</span>POST<span class="pl-pds">"</span></span>,
            <span class="pl-ent">"header"</span>: [
              {
                <span class="pl-ent">"key"</span>: <span class="pl-s"><span class="pl-pds">"</span>Content-Type<span class="pl-pds">"</span></span>,
                <span class="pl-ent">"value"</span>: <span class="pl-s"><span class="pl-pds">"</span>application/json<span class="pl-pds">"</span></span>
              }
            ],
            <span class="pl-ent">"body"</span>: {
              <span class="pl-ent">"mode"</span>: <span class="pl-s"><span class="pl-pds">"</span>raw<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{}<span class="pl-pds">"</span></span>
            },
            <span class="pl-ent">"url"</span>: {
              <span class="pl-ent">"raw"</span>: <span class="pl-s"><span class="pl-pds">"</span>{{base_url}}/api/cart<span class="pl-pds">"</span></span>,
              <span class="pl-ent">"host"</span>: [<span class="pl-s"><span class="pl-pds">"</span>{{base_url}}<span class="pl-pds">"</span></span>],
              <span class="pl-ent">"path"</span>: [<span class="pl-s"><span class="pl-pds">"</span>api<span class="pl-pds">"</span></span>, <span class="pl-s"><span class="pl-pds">"</span>cart<span class="pl-pds">"</span></span>]
            }
          }
        }
      ]
    }
  ]
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
  &quot;info&quot;: {
    &quot;name&quot;: &quot;FastAPI Shop API&quot;,
    &quot;description&quot;: &quot;Коллекция для тестирования API интернет-магазина&quot;,
    &quot;schema&quot;: &quot;https://schema.getpostman.com/json/collection/v2.1.0/collection.json&quot;
  },
  &quot;item&quot;: [
    {
      &quot;name&quot;: &quot;Health&quot;,
      &quot;item&quot;: [
        {
          &quot;name&quot;: &quot;Health Check&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;GET&quot;,
            &quot;header&quot;: [],
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/health&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;health&quot;]
            }
          },
          &quot;event&quot;: [
            {
              &quot;listen&quot;: &quot;test&quot;,
              &quot;script&quot;: {
                &quot;exec&quot;: [
                  &quot;pm.test(\&quot;Status code is 200\&quot;, function () {&quot;,
                  &quot;    pm.response.to.have.status(200);&quot;,
                  &quot;});&quot;,
                  &quot;&quot;,
                  &quot;pm.test(\&quot;Status is healthy\&quot;, function () {&quot;,
                  &quot;    var jsonData = pm.response.json();&quot;,
                  &quot;    pm.expect(jsonData.status).to.eql(\&quot;healthy\&quot;);&quot;,
                  &quot;});&quot;
                ]
              }
            }
          ]
        }
      ]
    },
    {
      &quot;name&quot;: &quot;Categories&quot;,
      &quot;item&quot;: [
        {
          &quot;name&quot;: &quot;Get All Categories&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;GET&quot;,
            &quot;header&quot;: [],
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/api/categories&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;api&quot;, &quot;categories&quot;]
            }
          },
          &quot;event&quot;: [
            {
              &quot;listen&quot;: &quot;test&quot;,
              &quot;script&quot;: {
                &quot;exec&quot;: [
                  &quot;pm.test(\&quot;Status code is 200\&quot;, function () {&quot;,
                  &quot;    pm.response.to.have.status(200);&quot;,
                  &quot;});&quot;,
                  &quot;&quot;,
                  &quot;pm.test(\&quot;Response is array\&quot;, function () {&quot;,
                  &quot;    var jsonData = pm.response.json();&quot;,
                  &quot;    pm.expect(jsonData).to.be.an(&#39;array&#39;);&quot;,
                  &quot;});&quot;,
                  &quot;&quot;,
                  &quot;if (pm.response.json().length &gt; 0) {&quot;,
                  &quot;    pm.environment.set(\&quot;category_id\&quot;, pm.response.json()[0].id);&quot;,
                  &quot;}&quot;
                ]
              }
            }
          ]
        },
        {
          &quot;name&quot;: &quot;Get Category by ID&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;GET&quot;,
            &quot;header&quot;: [],
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/api/categories/{{category_id}}&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;api&quot;, &quot;categories&quot;, &quot;{{category_id}}&quot;]
            }
          }
        },
        {
          &quot;name&quot;: &quot;Get Invalid Category&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;GET&quot;,
            &quot;header&quot;: [],
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/api/categories/9999&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;api&quot;, &quot;categories&quot;, &quot;9999&quot;]
            }
          },
          &quot;event&quot;: [
            {
              &quot;listen&quot;: &quot;test&quot;,
              &quot;script&quot;: {
                &quot;exec&quot;: [
                  &quot;pm.test(\&quot;Status code is 404\&quot;, function () {&quot;,
                  &quot;    pm.response.to.have.status(404);&quot;,
                  &quot;});&quot;
                ]
              }
            }
          ]
        }
      ]
    },
    {
      &quot;name&quot;: &quot;Products&quot;,
      &quot;item&quot;: [
        {
          &quot;name&quot;: &quot;Get All Products&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;GET&quot;,
            &quot;header&quot;: [],
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/api/products&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;api&quot;, &quot;products&quot;]
            }
          },
          &quot;event&quot;: [
            {
              &quot;listen&quot;: &quot;test&quot;,
              &quot;script&quot;: {
                &quot;exec&quot;: [
                  &quot;pm.test(\&quot;Status code is 200\&quot;, function () {&quot;,
                  &quot;    pm.response.to.have.status(200);&quot;,
                  &quot;});&quot;,
                  &quot;&quot;,
                  &quot;if (pm.response.json().products.length &gt; 0) {&quot;,
                  &quot;    pm.environment.set(\&quot;product_id\&quot;, pm.response.json().products[0].id);&quot;,
                  &quot;}&quot;
                ]
              }
            }
          ]
        },
        {
          &quot;name&quot;: &quot;Get Product by ID&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;GET&quot;,
            &quot;header&quot;: [],
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/api/products/{{product_id}}&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;api&quot;, &quot;products&quot;, &quot;{{product_id}}&quot;]
            }
          }
        },
        {
          &quot;name&quot;: &quot;Get Products by Category&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;GET&quot;,
            &quot;header&quot;: [],
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/api/products/category/{{category_id}}&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;api&quot;, &quot;products&quot;, &quot;category&quot;, &quot;{{category_id}}&quot;]
            }
          }
        }
      ]
    },
    {
      &quot;name&quot;: &quot;Cart&quot;,
      &quot;item&quot;: [
        {
          &quot;name&quot;: &quot;Add to Cart&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;POST&quot;,
            &quot;header&quot;: [
              {
                &quot;key&quot;: &quot;Content-Type&quot;,
                &quot;value&quot;: &quot;application/json&quot;
              }
            ],
            &quot;body&quot;: {
              &quot;mode&quot;: &quot;raw&quot;,
              &quot;raw&quot;: &quot;{\n  \&quot;product_id\&quot;: 1,\n  \&quot;quantity\&quot;: 2,\n  \&quot;cart\&quot;: {}\n}&quot;
            },
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/api/cart/add&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;api&quot;, &quot;cart&quot;, &quot;add&quot;]
            }
          },
          &quot;event&quot;: [
            {
              &quot;listen&quot;: &quot;test&quot;,
              &quot;script&quot;: {
                &quot;exec&quot;: [
                  &quot;pm.test(\&quot;Status code is 200\&quot;, function () {&quot;,
                  &quot;    pm.response.to.have.status(200);&quot;,
                  &quot;});&quot;,
                  &quot;&quot;,
                  &quot;pm.environment.set(\&quot;cart\&quot;, JSON.stringify(pm.response.json().cart));&quot;
                ]
              }
            }
          ]
        },
        {
          &quot;name&quot;: &quot;Get Cart Details&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;POST&quot;,
            &quot;header&quot;: [
              {
                &quot;key&quot;: &quot;Content-Type&quot;,
                &quot;value&quot;: &quot;application/json&quot;
              }
            ],
            &quot;body&quot;: {
              &quot;mode&quot;: &quot;raw&quot;,
              &quot;raw&quot;: &quot;{\n  \&quot;1\&quot;: 2,\n  \&quot;2\&quot;: 1\n}&quot;
            },
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/api/cart&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;api&quot;, &quot;cart&quot;]
            }
          }
        },
        {
          &quot;name&quot;: &quot;Update Cart Item&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;PUT&quot;,
            &quot;header&quot;: [
              {
                &quot;key&quot;: &quot;Content-Type&quot;,
                &quot;value&quot;: &quot;application/json&quot;
              }
            ],
            &quot;body&quot;: {
              &quot;mode&quot;: &quot;raw&quot;,
              &quot;raw&quot;: &quot;{\n  \&quot;product_id\&quot;: 1,\n  \&quot;quantity\&quot;: 5,\n  \&quot;cart\&quot;: {\n    \&quot;1\&quot;: 2,\n    \&quot;2\&quot;: 1\n  }\n}&quot;
            },
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/api/cart/update&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;api&quot;, &quot;cart&quot;, &quot;update&quot;]
            }
          }
        },
        {
          &quot;name&quot;: &quot;Remove from Cart&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;DELETE&quot;,
            &quot;header&quot;: [
              {
                &quot;key&quot;: &quot;Content-Type&quot;,
                &quot;value&quot;: &quot;application/json&quot;
              }
            ],
            &quot;body&quot;: {
              &quot;mode&quot;: &quot;raw&quot;,
              &quot;raw&quot;: &quot;{\n  \&quot;cart\&quot;: {\n    \&quot;1\&quot;: 5,\n    \&quot;2\&quot;: 1\n  }\n}&quot;
            },
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/api/cart/remove/1&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;api&quot;, &quot;cart&quot;, &quot;remove&quot;, &quot;1&quot;]
            }
          }
        },
        {
          &quot;name&quot;: &quot;Get Empty Cart&quot;,
          &quot;request&quot;: {
            &quot;method&quot;: &quot;POST&quot;,
            &quot;header&quot;: [
              {
                &quot;key&quot;: &quot;Content-Type&quot;,
                &quot;value&quot;: &quot;application/json&quot;
              }
            ],
            &quot;body&quot;: {
              &quot;mode&quot;: &quot;raw&quot;,
              &quot;raw&quot;: &quot;{}&quot;
            },
            &quot;url&quot;: {
              &quot;raw&quot;: &quot;{{base_url}}/api/cart&quot;,
              &quot;host&quot;: [&quot;{{base_url}}&quot;],
              &quot;path&quot;: [&quot;api&quot;, &quot;cart&quot;]
            }
          }
        }
      ]
    }
  ]
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Чек-лист тестирования</h2><a id="user-content-чек-лист-тестирования" class="anchor" aria-label="Permalink: Чек-лист тестирования" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D1%87%D0%B5%D0%BA-%D0%BB%D0%B8%D1%81%D1%82-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">✅ Базовые проверки</h3><a id="user-content--базовые-проверки" class="anchor" aria-label="Permalink: ✅ Базовые проверки" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#-%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B8"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Сервер запускается без ошибок</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Health check возвращает статус "healthy"</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> API доступен по адресу <code>http://localhost:8000</code></li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Документация доступна по <code>/api/docs</code></li>
</ul>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">✅ Категории</h3><a id="user-content--категории" class="anchor" aria-label="Permalink: ✅ Категории" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Получение списка всех категорий</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Получение категории по существующему ID</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Ошибка 404 для несуществующего ID</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Все поля присутствуют в ответе</li>
</ul>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">✅ Товары</h3><a id="user-content--товары" class="anchor" aria-label="Permalink: ✅ Товары" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%8B"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Получение списка всех товаров</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Получение товара по ID</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Фильтрация по категории</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Товар содержит информацию о категории</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Цены являются положительными числами</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Ошибка 404 для несуществующего товара</li>
</ul>
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto">✅ Корзина</h3><a id="user-content--корзина" class="anchor" aria-label="Permalink: ✅ Корзина" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#-%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D0%B0"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Добавление товара в пустую корзину</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Добавление нескольких товаров</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Увеличение количества существующего товара</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Обновление количества товара</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Удаление товара из корзины</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Получение детальной информации о корзине</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Правильный расчет subtotal и total</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Правильный подсчет items_count</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Ошибка при добавлении несуществующего товара</li>
<li class="task-list-item"><input type="checkbox" id="" disabled="" class="task-list-item-checkbox" aria-label="Incomplete task"> Ошибка при обновлении несуществующего товара в корзине</li>
</ul>
<hr>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Советы по тестированию</h2><a id="user-content-советы-по-тестированию" class="anchor" aria-label="Permalink: Советы по тестированию" href="https://github.com/s6ptember/fastapi-shop/blob/master/backend/test_commands.md#%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D1%8B-%D0%BF%D0%BE-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ol dir="auto">
<li>
<p dir="auto"><strong>Запускайте тесты последовательно</strong> - используйте Collection Runner для автоматического выполнения всех тестов</p>
</li>
<li>
<p dir="auto"><strong>Используйте переменные окружения</strong> - для переключения между dev/staging/production окружениями</p>
</li>
<li>
<p dir="auto"><strong>Сохраняйте результаты тестов</strong> - Postman позволяет экспортировать результаты в JSON</p>
</li>
<li>
<p dir="auto"><strong>Проверяйте время ответа</strong> - добавьте тесты на производительность</p>
</li>
<li>
<p dir="auto"><strong>Тестируйте граничные случаи</strong>:</p>
<ul dir="auto">
<li>Пустые запросы</li>
<li>Отрицательные числа</li>
<li>Очень большие значения</li>
<li>Некорректные типы данных</li>
</ul>
</li>
<li>
<p dir="auto"><strong>Используйте Pre-request Scripts</strong> - для подготовки тестовых данных</p>
</li>
<li>
<p dir="auto"><strong>Автоматизируйте</strong> - интегрируйте Postman тесты в CI/CD pipeline с помощью Newman</p>
</li>
</ol>
<hr>
<p dir="auto">Готово! Теперь у вас есть полное руководство по тестированию вашего API в Postman. 🚀</p>
</article></div><div class="d-none"></div></section></div></div></div> </div>  </div></div></div></div></div></div><div class="ScrollMarksContainer-module__scrollMarksContainer__Eu7uU" id="find-result-marks-container"></div><div class="d-none"></div><div class="d-none"></div></div> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA__R_1___">{"resolvedServerColorMode":"night"}</script></div>
</react-app>




  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer tmp-pt-7 tmp-pb-6 f6 color-fg-muted color-border-subtle p-responsive" role="contentinfo" hidden="">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="GitHub Homepage" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M10.226 17.284c-2.965-.36-5.054-2.493-5.054-5.256 0-1.123.404-2.336 1.078-3.144-.292-.741-.247-2.314.09-2.965.898-.112 2.111.36 2.83 1.01.853-.269 1.752-.404 2.853-.404 1.1 0 1.999.135 2.807.382.696-.629 1.932-1.1 2.83-.988.315.606.36 2.179.067 2.942.72.854 1.101 2 1.101 3.167 0 2.763-2.089 4.852-5.098 5.234.763.494 1.28 1.572 1.28 2.807v2.336c0 .674.561 1.056 1.235.786 4.066-1.55 7.255-5.615 7.255-10.646C23.5 6.188 18.334 1 11.978 1 5.62 1 .5 6.188.5 12.545c0 4.986 3.167 9.12 7.435 10.669.606.225 1.19-.18 1.19-.786V20.63a2.9 2.9 0 0 1-1.078.224c-1.483 0-2.359-.808-2.987-2.313-.247-.607-.517-.966-1.034-1.033-.27-.023-.359-.135-.359-.27 0-.27.45-.471.898-.471.652 0 1.213.404 1.797 1.235.45.651.921.943 1.483.943.561 0 .92-.202 1.437-.719.382-.381.674-.718.944-.943"></path>
</svg>
</a>
      <span>
        © 2026 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">


          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to community&quot;,&quot;label&quot;:&quot;text:community&quot;}" href="https://github.community/" data-view-component="true" class="Link--secondary Link">Community</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}">
       Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent text-left" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>



    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-locale="en" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none; --darkreader-inline-outline: initial;" data-darkreader-inline-outline="">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/KonstaNtinAleKseeVicHtheonly"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
      }
      .user-mention[href$="/KonstaNtinAleKseeVicHtheonly"]:before,
      .user-mention[href$="/KonstaNtinAleKseeVicHtheonly"]:after {
        content: '';
        display: inline-block;
        width: 2px;
      }
    </style><style class="darkreader darkreader--sync" media="screen"></style>


    </div>
    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true"></div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


<div class="sr-only mt-n1" id="screenReaderAnnouncementDiv" role="alert" data-testid="screenReaderAnnouncement" aria-live="assertive"></div><live-region><template shadowrootmode="open"><style class="darkreader darkreader--inline" media="screen">[data-darkreader-inline-bgcolor] {
  background-color: var(--darkreader-inline-bgcolor) !important;
}
[data-darkreader-inline-bgimage] {
  background-image: var(--darkreader-inline-bgimage) !important;
}
[data-darkreader-inline-border] {
  border-color: var(--darkreader-inline-border) !important;
}
[data-darkreader-inline-border-bottom] {
  border-bottom-color: var(--darkreader-inline-border-bottom) !important;
}
[data-darkreader-inline-border-left] {
  border-left-color: var(--darkreader-inline-border-left) !important;
}
[data-darkreader-inline-border-right] {
  border-right-color: var(--darkreader-inline-border-right) !important;
}
[data-darkreader-inline-border-top] {
  border-top-color: var(--darkreader-inline-border-top) !important;
}
[data-darkreader-inline-boxshadow] {
  box-shadow: var(--darkreader-inline-boxshadow) !important;
}
[data-darkreader-inline-color] {
  color: var(--darkreader-inline-color) !important;
}
[data-darkreader-inline-fill] {
  fill: var(--darkreader-inline-fill) !important;
}
[data-darkreader-inline-stroke] {
  stroke: var(--darkreader-inline-stroke) !important;
}
[data-darkreader-inline-outline] {
  outline-color: var(--darkreader-inline-outline) !important;
}
[data-darkreader-inline-stopcolor] {
  stop-color: var(--darkreader-inline-stopcolor) !important;
}
[data-darkreader-inline-bg] {
  background: var(--darkreader-inline-bg) !important;
}
[data-darkreader-inline-border-short] {
  border: var(--darkreader-inline-border-short) !important;
}
[data-darkreader-inline-border-bottom-short] {
  border-bottom: var(--darkreader-inline-border-bottom-short) !important;
}
[data-darkreader-inline-border-left-short] {
  border-left: var(--darkreader-inline-border-left-short) !important;
}
[data-darkreader-inline-border-right-short] {
  border-right: var(--darkreader-inline-border-right-short) !important;
}
[data-darkreader-inline-border-top-short] {
  border-top: var(--darkreader-inline-border-top-short) !important;
}
[data-darkreader-inline-invert] {
    filter: invert(100%) hue-rotate(180deg);
}</style><style class="darkreader darkreader--override" media="screen">.vimvixen-hint {
    background-color: var(--darkreader-background-ffd76e, #684b00) !important;
    border-color: var(--darkreader-background-c59d00, #9e7e00) !important;
    color: var(--darkreader-text-302505, #d7d4cf) !important;
}
#vimvixen-console-frame {
    color-scheme: light !important;
}
::placeholder {
    opacity: 0.5 !important;
}
#edge-translate-panel-body,
.MuiTypography-body1,
.nfe-quote-text {
    color: var(--darkreader-neutral-text) !important;
}
gr-main-header {
    background-color: var(--darkreader-background-add8e6, #1b4958) !important;
}
.tou-z65h9k,
.tou-mignzq,
.tou-1b6i2ox,
.tou-lnqlqk {
    background-color: var(--darkreader-neutral-background) !important;
}
.tou-75mvi {
    background-color: var(--darkreader-background-cfecf5, #0f3a47) !important;
}
.tou-ta9e87,
.tou-1w3fhi0,
.tou-1b8t2us,
.tou-py7lfi,
.tou-1lpmd9d,
.tou-1frrtv8,
.tou-17ezmgn {
    background-color: var(--darkreader-background-f5f5f5, #1e2021) !important;
}
.tou-uknfeu {
    background-color: var(--darkreader-background-faedda, #432c09) !important;
}
.tou-6i3zyv {
    background-color: var(--darkreader-background-85c3d8, #245d70) !important;
}
div.mermaid-viewer-control-panel .btn {
    background-color: var(--darkreader-neutral-background);
    fill: var(--darkreader-neutral-text);
}
svg g rect.er {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.entityBox {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.attributeBoxOdd {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.attributeBoxEven {
    fill: var(--darkreader-selection-background);
    fill-opacity: 0.8 !important;
}
svg rect.er.relationshipLabelBox {
    fill: var(--darkreader-neutral-background) !important;
}
svg g g.nodes rect,
svg g g.nodes polygon {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.task {
    fill: var(--darkreader-selection-background) !important;
}
svg line.messageLine0,
svg line.messageLine1 {
    stroke: var(--darkreader-neutral-text) !important;
}
div.mermaid .actor {
    fill: var(--darkreader-neutral-background) !important;
}
mitid-authenticators-code-app > .code-app-container {
    background-color: white !important;
    padding-top: 1rem;
}
iframe#unpaywall[src$="unpaywall.html"] {
    color-scheme: light !important;
}
select {
    --darkreader-bg--form-control-background-color: rgba(22, 22, 22, 0) !important;
}
body#tumblr {
    --darkreader-bg--secondary-accent: 31, 32, 34 !important;
    --darkreader-bg--white: 23, 23, 23 !important;
    --darkreader-text--black: 228, 224, 218 !important;
}
:host {
    --d2l-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-button-icon-background-color-hover: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-color-ferrite: var(--darkreader-neutral-text) !important;
    --d2l-color-sylvite: var(--darkreader-bg--d2l-color-sylvite) !important;
    --d2l-dropdown-background-color: var(--darkreader-neutral-background) !important;
    --d2l-dropdown-border-color: var(--darkreader-border--d2l-color-mica) !important;
    --d2l-input-backgroud-color: var(--darkreader-neutral-background) !important;
    --d2l-menu-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-tooltip-background-color: var(--darkreader-neutral-background) !important;
    --d2l-tooltip-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
:host([_floating]) .d2l-floating-buttons-container {
    background-color: var(--darkreader-neutral-background) !important;
    border-top-color: var(--darkreader-border--d2l-color-mica) !important;
    opacity: 0.88 !important;
}
d2l-card {
    background: var(--darkreader-neutral-background) !important;
    border-color: var(--darkreader-border--d2l-color-gypsum) !important;
}
d2l-dropdown-content > div,
d2l-menu-item {
    background-color: var(--darkreader-neutral-background) !important;
    border-radius: 10px !important;
}
d2l-empty-state-simple {
    border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-button-filter > ul > li > a.vui-button {
    border-color: var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-label-text:has(.d2l-button-subtle-content):hover,
.d2l-label-text:has(.d2l-button-subtle-content):focus,
.d2l-label-text:has(.d2l-button-subtle-content):active {
    background-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-navigation-centerer {
    color: inherit !important;
}
.d2l-tabs-layout {
    border-color: var(--darkreader-border--d2l-color-gypsum) !important;
}
.d2l-input,
.d2l-calendar-date,
.d2l-htmleditor-container {
    background-color: var(--darkreader-neutral-background) !important;
}
.d2l-collapsible-panel {
    border: 1px solid var(--darkreader-border--d2l-color-mica) !important;
    border-radius: 0.4rem !important;
}
.d2l-collapsible-panel-divider {
    border-bottom: 1px solid var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-w2d-flex {
    border-bottom: 2px solid var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-collapsible-panel scrolled,
.d2l-collapsible-panel-header,
.d2l-w2d-collection-fixed {
    background-color: var(--darkreader-neutral-background) !important;
}
.d2l-loading-spinner-bg {
    fill: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-loading-spinner-bg-stroke {
    stroke: var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-loading-spinner-wrapper svg path,
.d2l-loading-spinner-wrapper svg circle {
    fill: var(--darkreader-neutral-background) !important;
}
.d2l-twopanelselector-side.d2l-twopanelselector-side-sep {
    background: var(--darkreader-bg--d2l-color-mica) !important;
}
.d2l-le-TreeAccordionItem-anchor::before {
    background: var(--darkreader-bg--d2l-color-corundum) !important;
}
table[class|="moz-header"] {
    background: none;
}
*[style*="color: rgba(0,0,0,"],
*[style*="color: rgba(0, 0, 0,"],
*[style*="color:#000"],
*[style*="color:black"],
*[style*="color:#282828"],
*[style*="color:#444"] {
    color: var(--darkreader-neutral-text) !important;
}
*[style*="background:#fff"],
*[style*="background-color:#fff"] {
    background: var(--darkreader-neutral-background) !important;
}
*[bgcolor="#F5F5F5"],
*[style*="background-color: #F5F5F5"] {
    background: var(--darkreader-background-f5f5f5, #1e2021) !important;
}
body[style*="background: rgb(255, 255, 255) !important"] *:not(a),
.body[style*="background-color: rgb(254, 254, 254) !important"] *:not(a) {
    background-color: var(--darkreader-neutral-background) !important;
}
div[style*="www.gstatic.com/android/"] {
    background: none !important;
}
*[style*="background:#f9f9f9"] {
    background: var(--darkreader-background-f9f9f9, #1b1e1f) !important;
}
body.mediawiki.skin-vector #mw-page-base {
    background-image: none !important;
}
embed[type="application/pdf"][src="about:blank"] { filter: invert(100%) contrast(90%); }
.blob-code-inner,
.blob-num,
.cm-s-github-light .CodeMirror-lines,
.CodeMirror pre > span,
.CodeMirror,
.CodeMirror-dialog input,
.CodeMirror-hints,
.CodeMirror-linenumber,
.CodeMirror-lines,
.commit .sha,
.commit .sha-block,
.commit-desc pre,
.commit-ref,
.commit-tease-sha,
.export-phrase pre,
.file-info,
.FormControl-input.FormControl-monospace,
.FormControl-select.FormControl-monospace,
.FormControl-textarea.FormControl-monospace,
.input-monospace,
.markdown-body .footnotes .data-footnote-backref g-emoji,
.pr-1 > code > a,
.react-blob-print-hide,
.react-code-text,
.react-code-view-edit .cm-s-github-light .CodeMirror-lines,
.text-mono *,
.text-mono,
.two-factor-recovery-codes,
[aria-labelledby*="codemirror"] *,
[class*="blob-code"] *,
code > a[class="Link--secondary"],
section[aria-labelledby*="file-name-id"] > div > div *,
span.commit-ref > a > *,
span.commit-ref > a {
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace !important;
}
.markdown-body code,
.markdown-title code {
    background-color: var(--darkreader-text-1b1f231a, rgba(212, 209, 203, 0.1)) !important;
}
.markdown-body pre code {
    background-color: transparent !important;
}
.refined-github .dashboard .js-all-activity-header + div {
    background-color: var(--darkreader-background-e4e5e9, #26292b) !important;
    border-color: var(--darkreader-background-bbc1c9, #3a3f42) !important;
}
.refined-github .dashboard-rollup-items .body {
    border-top-color: var(--darkreader-background-bbc1c9, #3a3f42) !important;
}
.refined-github .reaction-summary-item a {
    box-shadow: 0 0 0 2px var(--darkreader-background-ffffff, #181a1b) !important;
}
.refined-github button.reaction-summary-item {
    border-bottom: rgb(77, 172, 253) !important;
    border-top-color: rgb(52, 59, 68) !important;
}
.js-site-search-form {
    background-color: #ffffff1a !important;
    border-radius: 2pt !important;
}
.blob-num:not(.cc-coverage-covered-border):not(.cc-coverage-missed-border) {
    border-right: 0 !important;
}
.cc-issue-description {
    color: #24292e !important;
}
.cc-readup-background {
    background-color: rgb(28, 30, 31) !important;
}
.cc-readup-content {
    border-left: 1px solid grey !important;
    color: rgb(216, 214, 208) !important;
}
.cc-readup-content blockquote {
    border-left: 3px solid dimgrey !important;
}
.cc-pr__link-text {
    color: darkgrey !important;
}
.cc-pr__tooltip {
    background-color: rgb(28, 30, 31) !important;
    color: darkgrey !important;
}
.jfk-bubble,
.octotree-sidebar,
.cc-pr__logo,
.cc-octicon,
#network canvas,
img.network-tree {
    filter: invert(94.4%) hue-rotate(180deg) contrast(90%) !important;
}
#commit-activity-detail > svg {
    fill: var(--darkreader-text-000000, #e8e6e3) !important;
}
.ContributionCalendar-day,
.ContributionCalendar-day[data-level="0"] {
    fill: var(--color-calendar-graph-day-bg) !important;
}
.ContributionCalendar-day[data-level="1"] {
    fill: var(--color-calendar-graph-day-L1-bg) !important;
}
.ContributionCalendar-day[data-level="2"] {
    fill: var(--color-calendar-graph-day-L2-bg) !important;
}
.ContributionCalendar-day[data-level="3"] {
    fill: var(--color-calendar-graph-day-L3-bg) !important;
}
.ContributionCalendar-day[data-level="4"] {
    fill: var(--color-calendar-graph-day-L4-bg) !important;
}
.day,
.day[data-Count="0"] {
    fill: var(--color-calendar-graph-day-bg) !important;
}
.day[data-Count="1"] {
    fill: var(--color-calendar-graph-day-L1-bg) !important;
}
.day[data-Count="2"] {
    fill: var(--color-calendar-graph-day-L2-bg) !important;
}
.day[data-Count="3"] {
    fill: var(--color-calendar-graph-day-L3-bg) !important;
}
.day[data-Count="4"] {
    fill: var(--color-calendar-graph-day-L4-bg) !important;
}
:root {
    --color-calendar-graph-day-bg: var(--darkreader-background-ebedf0, #222526) !important;
    --color-calendar-graph-day-L1-bg: var(--darkreader-background-9be9a8, #166634) !important;
    --color-calendar-graph-day-L2-bg: var(--darkreader-background-40c463, #2f9a5f) !important;
    --color-calendar-graph-day-L3-bg: var(--darkreader-background-30a14e, #26813e) !important;
    --color-calendar-graph-day-L4-bg: var(--darkreader-text-216e39, #8bdca4) !important;
    --color-previewable-comment-form-bg: var(--darkreader-neutral-background) !important;
}
.Box-row--yellow {
    background-color: var(--darkreader-background-fffbdd, #362f00) !important;
}
.merge-status-list {
    border-color: var(--darkreader-background-c0c5c7, #3a3e41) !important;
}
.user-has-reacted {
    background-color: rgba(17, 88, 199, 0.2) !important;
}
.hx_IssueLabel,
span[class*="TokenBase"] {
    background: rgba(var(--label-r),var(--label-g),var(--label-b),var(--background-alpha)) !important;
    border-color: hsla(var(--label-h),calc(var(--label-s) * 1%),calc((var(--label-l) + var(--lighten-by)) * 1%),var(--border-alpha)) !important;
    color: hsl(var(--label-h),calc(var(--label-s) * 1%),calc((var(--label-l) + var(--lighten-by)) * 1%)) !important;
}
.header-search-input {
    border: 0 !important;
}
.HeaderMenu-link--sign-in {
    border: 0 !important;
}
.timeline-comment--caret.current-user::after {
    --color-current-user-tip-bg: var(--darkreader-bg--color-box-bg-info) !important;
}
.timeline-comment--caret.current-user::before {
    background-color: var(--darkreader-border--color-box-border-info) !important;
}
@media screen and (min-width: 1012px) {
    markdown-toolbar.border-lg-top-0 {
        border-top: 1px solid var(--darkreader-border--color-border-primary) !important;
    }
}
@media screen and (max-width: 767px) {
    div.tabnav--responsive button.tabnav-tab {
        --color-border-primary: var(--darkreader-border--color-border-primary) !important;
    }
}
.TimelineItem-badge[style^="background-color: var(--color-timeline-merged-bg)"] {
    background-color: var(--color-timeline-merged-bg) !important;
}
.ContributionCalendar-label {
    --color-text-primary: var(--darkreader-neutral-text) !important;
}
article div[style^="background: linear-gradient"] {
    background: linear-gradient(to top, var(--darkreader-bg--color-bg-primary), transparent) !important;
}
.ͼ5 .cm-content,
.ͼ5 .cm-panel.cm-search > button {
    background-color: var(--darkreader-neutral-background) !important;
}</style><style class="darkreader darkreader--invert" media="screen">.jfk-bubble.gtx-bubble, .captcheck_answer_label > input + img, span#closed_text > img[src^="https://www.gstatic.com/images/branding/googlelogo"], span[data-href^="https://www.hcaptcha.com/"] > #icon, img.Wirisformula, a[data-testid="headerMediumLogo"]>svg, .d2l-navigation-link-image-container, .d2l-iframe-loading-container, div.mc-ip-hide[style*="background: rgb(255, 255, 255) !important"], [style*="color: rgb(0, 0, 1) !important;"], [src="https://github.githubassets.com/images/modules/site/icons/footer/github-logo.svg"], [src^="https://github.githubassets.com/images/modules/site/home/community-sponsor-"], [src^="https://github.githubassets.com/images/modules/site/home/community-readme-"], [src^="https://github.githubassets.com/images/modules/site/home/community-discussions-"], [src="https://github.githubassets.com/images/modules/site/home/dependabot-merge.png"], [src="https://github.githubassets.com/images/modules/site/home/dependabot-pr.png"], [src="https://github.githubassets.com/images/modules/site/home/gh-desktop.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-merge.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-comment.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-description.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-screen.png"], [src="https://github.githubassets.com/images/modules/site/home/enterprise-city-w-logos.jpg"], [src="https://github.githubassets.com/images/modules/site/codespaces/codespaces-icon.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/dependency-rust.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/dependency-3.png"], [src^="https://github.githubassets.com/images/modules/site/codespaces/dependencies-"], [src="https://github.githubassets.com/images/modules/site/codespaces/commit-3.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/extensions-1.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/extensions-2.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/commit-workflow.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/workflow-view.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/code.png"], [src="https://github.githubassets.com/images/email/explore/explore-gradient-icon.png"], [src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/collections/learn-to-code/learn-to-code.png"], .js-viewport-aware-video.color-bg-primary.width-full.d-block.codespaces-hero-video, .build-in-animate.position-relative.mb-6-fluid.box-shadow-active-mktg.mx-auto.home-mobile-iphone.build-in-slideY.js-build-in > .js-viewport-aware-video.width-full, .overflow-hidden.position-relative.box-shadow-active-border-mktg.rounded-2-fluid.color-bg-primary.build-in-scale-fade.js-build-in-item, .build-in-animate.overflow-hidden.box-shadow-active-border-mktg.rounded-2-fluid.position-relative.home-workflow-comp.js-build-in-item, .mx-lg-auto.col-lg-7.col-12, #hero-section-brand-heading {
    filter: invert(100%) hue-rotate(180deg) contrast(90%) !important;
}</style>
<style>
:host {
  border: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  white-space: nowrap;
  width: 1px;
}
</style><style class="darkreader darkreader--sync" media="screen"></style>
<div id="polite" aria-live="polite" aria-atomic="true">nginx content loaded</div>
<div id="assertive" aria-live="assertive" aria-atomic="true"></div>
</template></live-region></body></html>