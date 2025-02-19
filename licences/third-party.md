# Third Party Licences

* toc
{:toc}

This page references the licences for all third party libraries and data shipped with MapLink Pro.

## Third Party Libraries

<table>
{% for item in site.data.thirdpartylicences.libs_url %}
<tr>
<td>{{ item.title }}</td>
<td>{{ item.version }}</td>
<td><a href="{{ item.url }}">{{ item.url }}</a></td>
</tr>
{% endfor %}
{% for item in site.data.thirdpartylicences.libs_message %}
<tr>
<td>{{ item.title }}</td>
<td>{{ item.version }}</td>
<td>{{ item.message }}</td>
</tr>
{% endfor %}
</table>

## Third Party Data & Maps

<table>
{% for item in site.data.thirdpartylicences.data_url %}
<tr>
<td>{{ item.title }}</td>
<td><a href="{{ item.url }}">{{ item.url }}</a></td>
</tr>
{% endfor %}
{% for item in site.data.thirdpartylicences.data_message %}
<tr>
<td>{{ item.title }}</td>
<td>{{ item.message }}</td>
</tr>
{% endfor %}
</table>

