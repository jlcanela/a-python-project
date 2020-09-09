#!/bin/bash
echo pylint:
pylint src

echo pyright:
npx pyright

echo test coverage:
coverage run --source=. -m pytest tests
coverage report
coverage html