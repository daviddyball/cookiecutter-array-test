import cookiecutter from cookiecutter.main

ARRAY = '{{ cookiecutter.array }}'

cookiecutter('./', extra_context={"arrayValue": {"value": ARRAY}})
