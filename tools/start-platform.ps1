# ============================================================
# EV Fleet Monitoring Platform
# Bootstrap Manager
# ============================================================

Clear-Host

$Root = Split-Path $PSScriptRoot -Parent

$Venv = Join-Path $Root ".venv\Scripts\Activate.ps1"
$Functions = Join-Path $Root "cloud\functions_app"

Write-Host ""
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host " EV Fleet Monitoring Platform" -ForegroundColor White
Write-Host " Bootstrap Manager" -ForegroundColor White
Write-Host "==============================================" -ForegroundColor Cyan
Write-Host ""

# ------------------------------------------------------------
# Virtual Environment
# ------------------------------------------------------------

if (!(Test-Path $Venv))
{
    Write-Host "Virtual Environment not found." -ForegroundColor Red
    exit
}

# ------------------------------------------------------------
# Mosquitto
# ------------------------------------------------------------

Write-Host "[1/4] Starting Mosquitto..." -ForegroundColor Yellow

$mosquitto = Get-Process mosquitto -ErrorAction SilentlyContinue

if ($mosquitto)
{
    Write-Host "Mosquitto already running." -ForegroundColor Green
}
else
{
    Start-Process powershell `
        -ArgumentList @(
            "-NoExit",
            "-Command",
            "mosquitto -v"
        )
}

Start-Sleep 2

Write-Host "OK" -ForegroundColor Green
Write-Host ""

Write-Host "[2/4] Starting Azure Functions..." -ForegroundColor Yellow

Start-Process powershell `
    -WorkingDirectory $Functions `
    -ArgumentList @(
        "-NoExit",
        "-Command",
        "func start"
    )

Start-Sleep 5

Write-Host "OK" -ForegroundColor Green

# ------------------------------------------------------------
# Edge Gateway
# ------------------------------------------------------------

Write-Host "[3/4] Starting Edge Gateway..." -ForegroundColor Yellow

Start-Process powershell `
    -ArgumentList @(
        "-NoExit",
        "-Command",
@"
Set-Location "$Root"
& "$Venv"
python -m edge_gateway.gateway
"@
)

Start-Sleep 2

Write-Host "OK" -ForegroundColor Green
Write-Host ""

# ------------------------------------------------------------
# Fleet Simulator
# ------------------------------------------------------------

Write-Host "[4/4] Starting Fleet Simulator..." -ForegroundColor Yellow

Start-Process powershell `
    -ArgumentList @(
        "-NoExit",
        "-Command",
@"
Set-Location "$Root"
& "$Venv"
python -m fleet_simulator.main
"@
)

Start-Sleep 2

Write-Host "OK" -ForegroundColor Green

Write-Host ""
Write-Host "==============================================" -ForegroundColor Green
Write-Host " Platform Started Successfully" -ForegroundColor Green
Write-Host "==============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Grafana        : http://localhost:3000"
Write-Host "Azure Function : http://localhost:7071"
Write-Host "Fleet Summary  : http://localhost:7071/api/fleet/summary"
Write-Host ""