---
title: Documentos
comments: true
permalink: /docs/
---

<!-- Programas electorales (manifestos) -->
{% assign documents = site.data.documents | where: 'type', "manifesto" | sort: "publication_date" %}

<h6 class="border-bottom pb-2">Programas electorales</h6>
<div class="row pt-2">
    {% include documents_list.html %}
</div>

<br>
<!-- Acuerdos de gobierno (goverment agreements) -->
{% assign documents = site.data.documents | where: 'type', "goverment_agreement" | sort: "publication_date" %}

<h6 class="border-bottom pb-2">Acuerdos de Gobierno</h6>
<div class="row pt-2">
    {% include documents_list.html %}
</div>
