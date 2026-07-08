# --------------------------------------------------------
# Check formatting, import order, linting, and run tests
# --------------------------------------------------------

Write-Host "Run Import Sorting..."
isort .

Write-Host "Formatting..."
black .

Write-Host "Linting..."
flake8 .

Write-Host "Running tests..."
pytest