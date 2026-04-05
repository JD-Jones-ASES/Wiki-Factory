---
title: "Random Hymn"
type: overview
aliases: ["Random", "Surprise Me"]
tags: []
created: 2026-04-05
updated: 2026-04-05
source_refs: []
related: []
status: complete
confidence: high
---

> [[_overview|Home]] > Random Hymn

# Random Hymn

Taking you to a random hymn...

<div id="random-status" style="text-align: center; padding: 2rem; color: var(--darkgray);">
  <p style="font-size: 1.2rem;">Finding a hymn for you...</p>
</div>

<script>
(async function() {
  try {
    // Quartz generates a contentIndex at the site root
    const base = document.querySelector("base")?.href || window.location.origin;
    const res = await fetch(new URL("contentIndex.json", base));
    const index = await res.json();

    // Filter for hymn pages (slugs containing "hymns/Hymn_")
    const hymnSlugs = Object.keys(index).filter(slug =>
      slug.includes("hymns/Hymn_")
    );

    if (hymnSlugs.length > 0) {
      const randomSlug = hymnSlugs[Math.floor(Math.random() * hymnSlugs.length)];
      window.location.href = new URL(randomSlug, base).href;
    } else {
      document.getElementById("random-status").innerHTML =
        '<p>Could not find hymn pages. <a href="./Hymns_Overview">Browse all hymns</a> instead.</p>';
    }
  } catch (e) {
    document.getElementById("random-status").innerHTML =
      '<p>Something went wrong. <a href="./Hymns_Overview">Browse all hymns</a> instead.</p>';
  }
})();
</script>
