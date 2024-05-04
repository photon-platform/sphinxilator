% name: Article
% def: post_date=$(date +%m/%d/%Y)
% def: author="/phi"
% def: collection_name="Articles"
---
title: ${title}
subtitle: ${subtitle}
date: ${post_date}
author: ${author}
content:
    title: ${collection_name}
    items: '@self.children'
taxonomy:
    photon:
    category: 
    tag: 
---

${summary}

===


