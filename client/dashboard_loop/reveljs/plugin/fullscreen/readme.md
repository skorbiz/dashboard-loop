Fullscreen

A plugin for Reveal.js allowing allowing to use the entire space available for slides.

Check out the demo
Setup

To use the plugin include

<!-- Fullscreen plugin -->
<script src="https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/fullscreen/plugin.js"></script>

to the header of your presentation and configure reveal.js and the plugin by

Reveal.initialize({
  // ...
  plugins: [ RevealFullscreen ],
  // ...
});

Usage

In markdown you can set the data-fullscreen attribute for a slide and make an element stretch to the space available by

<!-- .slide: data-fullscreen="true"  -->

### Embedded online content

<iframe class="stretch" src="https://www.youtube.com/embed/5xAgp6i9lUQ?rel=0" frameborder="0" allowfullscreen></iframe>

License

MIT licensed

Copyright (C) 2023 Asvin Goel
