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
# Environment Validation
# ------------------------------------------------------------

if (!(Test-Path $Venv)) {
    Write-Host "[ERROR] Virtual Environment not found." -ForegroundColor Red
    exit
}

if (!(Test-Path $Functions)) {
    Write-Host "[ERROR] Azure Functions project not found." -ForegroundColor Red
    exit
}

# ------------------------------------------------------------
# Mosquitto
# ------------------------------------------------------------

Write-Host "[1/4] Starting Mosquitto..." -ForegroundColor Yellow

if (Get-Process mosquitto -ErrorAction SilentlyContinue) {
    Write-Host "    [OK] Mosquitto already running." -ForegroundColor Green
}
else {
    Start-Process powershell `
        -ArgumentList @(
        "-NoExit",
        "-Command",
        "mosquitto -v"
    )

    Start-Sleep 2

    Write-Host "    [OK] Mosquitto Broker started." -ForegroundColor Green
}

Write-Host ""

# ------------------------------------------------------------
# Azure Functions
# ------------------------------------------------------------

Write-Host "[2/4] Starting Azure Functions..." -ForegroundColor Yellow

if (Get-Process func -ErrorAction SilentlyContinue) {
    Write-Host "    [OK] Azure Functions already running." -ForegroundColor Green
}
else {
    Start-Process powershell `
        -ArgumentList @(
        "-NoExit",
        "-Command",
        @"
Set-Location "$Functions"
& "$Venv"
func start
"@
    )

    Start-Sleep 5

    Write-Host "    [OK] Azure Functions Runtime started." -ForegroundColor Green
}

Write-Host ""

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

Write-Host "    [OK] Edge Gateway started." -ForegroundColor Green
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

Write-Host "    [OK] Fleet Simulator started." -ForegroundColor Green
Write-Host ""

# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

Write-Host "==========================================================" -ForegroundColor Green
Write-Host "        EV Fleet Monitoring Platform Ready" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
Write-Host ""

Write-Host "Services" -ForegroundColor Cyan
Write-Host "--------" -ForegroundColor Cyan
Write-Host "  [OK] Mosquitto Broker" -ForegroundColor Green
Write-Host "  [OK] Azure Functions" -ForegroundColor Green
Write-Host "  [OK] Edge Gateway" -ForegroundColor Green
Write-Host "  [OK] Fleet Simulator" -ForegroundColor Green
Write-Host ""

Write-Host "Architecture" -ForegroundColor Cyan
Write-Host "           ------------" -ForegroundColor Cyan
Write-Host "           Fleet Simulator"
Write-Host "              |"
Write-Host "              v"
Write-Host "           MQTT Broker"
Write-Host "              |"
Write-Host "              v"
Write-Host "           Edge Gateway"
Write-Host "              |"
Write-Host "              v"
Write-Host "           Azure IoT Hub"
Write-Host "              |"
Write-Host "              v"
Write-Host "           Azure Functions"
Write-Host "              |"
Write-Host "              v"
Write-Host "           Cosmos DB"
Write-Host "              |"
Write-Host "              v"
Write-Host "           Grafana"
Write-Host ""

Write-Host "Endpoints" -ForegroundColor Cyan
Write-Host "---------" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Azure Functions      : http://localhost:7071"
Write-Host "------------------------------------" -ForegroundColor Cyan
Write-Host "REST APIs Endpoints"
Write-Host "------------------------------------" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Fleet Summary API    : api/fleet/summary"
Write-Host "  Dashboard Vehicles   : api/dashboard/vehicles"
Write-Host "  Dashboard Trends     : api/dashboard/trends"
Write-Host ""
Write-Host "------------------------------------" -ForegroundColor Cyan
Write-Host "  Grafana Dashboard    : http://localhost:3000"
Write-Host ""

Write-Host "Platform started successfully." -ForegroundColor Green
Write-Host ""