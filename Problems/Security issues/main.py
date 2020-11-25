template = """
<form action="like" method="post">
  {% csrf_token %}
  <input type="submit" value="👍">
</form>
"""
