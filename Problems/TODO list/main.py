template = """
<html>
  <ul>
  {%for todo in todos %}
    <li> {{todo }} </li>
  {%endfor %}
  </ul>
</html>
"""
