---
title: Temas
comments: true
permalink: /statements-topics/
layout: document
---
<!-- all topics -->
<!-- TODO: use topics.yaml to show all topics as a structured document -->

{% assign toc = site.data.categorization.topics %}
{% assign topics = site.data.topics %}

<div data-bs-spy="scroll" data-bs-target="#TableOfContents" class="container-fluid my-3">
    
    {% include document_search.html %}

    <div class="container-xxl bd-gutter mt-3 my-md-4 bd-layout">
        <main class="bd-main">
            <div class="bd-intro pt-2 ps-lg-2">
                <div class="d-md-flex flex-md-row-reverse align-items-center justify-content-between">
                    <h2 class="bd-title mb-0" id="content"> Todas las declaraciones por temática</h2>
                </div>
                <p class="bd-lead">{{ doc.description }}</p>
                <hr class="d-none d-md-block my-2">
            </div>

            <!-- TOC -->
            <!-- TODO:  -->
            

            <!-- CONTENT -->
            

        </main>
    </div>
</div>