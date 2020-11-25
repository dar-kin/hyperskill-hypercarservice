template = """
  {% extends "blog/contacts.html" %}
  {% block contacts %} {{ block.super }} {% include "blog/social.html" %} {% endblock %}
"""
