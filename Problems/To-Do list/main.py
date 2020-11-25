template = """
<html>
  <div> You have {{ todos|length }} tasks to do: </div>
  <div> {{ todos|join:"<br/>" }} </div>
</html>
"""
