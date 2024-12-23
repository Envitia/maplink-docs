# Envitia MapLink Pro

Envitia’s software technology for mission system developers, enabling them to create high performance geospatial intelligence, situational awareness and map-based systems. Feature rich and proven in demanding operational systems, Envitia’s MapLink Pro provides system integrators and OEMs with the application control and flexibility they need while minimising delivery time and cost.

# Getting Started
## Installation
- [Get a trial version of MapLink Pro](https://forms.office.com/e/Lr7jN9TCC0).
- Our [Quick Start Guide](./pdf/MapLink Pro Quick Start Guide.pdf) will see you through the process of getting started.

## Samples
MapLink Pro comes installed with a variety of sample applications to get you started quickly.
You can also view our sample code and tips in our [GitHub repos](https://github.com/envitia).

## Platform Requirements
MapLink Pro has APIs for [C++](https://www.envitia.com/technologies/products/maplink-pro/userguide/index.html), .Net and Java and can be used on Windows, Linux and Android.

## Resources
- [Envitia MapLink Pro API Documentation](https://www.envitia.com/technologies/products/maplink-pro/userguide/index.html)
- [Technical Support](https://support.envitia.com)
- [Support Pages](./pages/support/support.md)

# Docs
<ul>
    {% for item in site.data.docs.docs %}
    <li>
    <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
    </li>
    {% endfor %}
</ul>