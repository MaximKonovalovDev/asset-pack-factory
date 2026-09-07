# Ship lanes. One file, many funcs. Simple words, numbers in code only.
function Get-ShipBase {
  [PSCustomObject]@{
    id = "pack-id"; title = "Pack title"; blurb = "Short blurb"
    price = ""; tags = @("prop"); aiTag = ""
    files = @("manifest.json"); upload = ""
  }
}

function Get-ShipListingText($lane) {
  "Title: $($lane.title)`nPrice: $($lane.price)`nFee: $($lane.fee)`nKeep: $($lane.keep)`nAI tag: $($lane.aiTag)`nFiles: $($lane.files -join ', ')`nUpload: $($lane.upload)`nBlurb: $($lane.blurb)"
}

function Get-FabLane {
  $b = Get-ShipBase
  $b | Add-Member -NotePropertyMembers @{
    site = "fab"; fee = "12%"; keep = "88%"
    price = '$19.99'; aiTag = "Fab portal AI-generated checkbox"
    files = @("fab-listing.txt","manifest.json","pack.zip","thumb.png")
    upload = "Fab portal web upload of pack.zip"
  } -Force; $b
}

function Get-UnityLane {
  $b = Get-ShipBase
  $b | Add-Member -NotePropertyMembers @{
    site = "unity"; fee = "30%"; keep = "70%"
    price = '$24.99, floor $4.99'; aiTag = "Publisher portal AI declaration"
    files = @("unity-listing.txt","manifest.json","pack.unitypackage","thumb.png")
    upload = "Unity Publisher portal upload of pack.unitypackage"
  } -Force; $b
}

function Get-SlMarketLane {
  $b = Get-ShipBase
  $b | Add-Member -NotePropertyMembers @{
    site = "sl-market"; fee = "10%"; keep = "90%"
    price = 'L$990'; aiTag = "Listing text tag [AI-assisted]"
    files = @("sl-market-listing.txt","manifest.json","pack.zip","thumb.png")
    upload = "marketplace.secondlife.com web upload"
  } -Force; $b
}

function Get-RobloxLane {
  $b = Get-ShipBase
  $b | Add-Member -NotePropertyMembers @{
    site = "roblox"; fee = "30% plus 750 Robux upload fee"; keep = "70%"
    price = "150 Robux, floor near 50"; aiTag = "Creator Hub AI use answer"
    files = @("roblox-listing.txt","manifest.json","pack.rbxm","thumb.png")
    upload = "Creator Dashboard upload of pack.rbxm"
  } -Force; $b
}

function Get-ItchLane {
  param([string]$User = "user", [string]$Game = "game", [string]$Channel = "win-64", [string]$Ver = "1.0.0")
  $b = Get-ShipBase
  $b | Add-Member -NotePropertyMembers @{
    site = "itch"; fee = "10% default, you set 0 to 100%"; keep = "90% at default"
    price = '$9.99, can be $0'; aiTag = "Edit page tag ai-generated"
    files = @("itch-listing.txt","manifest.json","pack.zip")
    upload = "butler push ./out ${User}/${Game}:${Channel} --userversion $Ver"
  } -Force; $b
}

function Get-VaultLane {
  $b = Get-ShipBase
  $b | Add-Member -NotePropertyMembers @{
    site = "vault"; fee = "Patreon 8% plus 2.9% plus 30c; Ko-fi 0% plus processing"; keep = "about 89% on Patreon, near 97% on Ko-fi"
    price = '$5 tier, $6 shop'; aiTag = "Post tag ai-assisted"
    files = @("patreon-post.txt","kofi-post.txt","manifest.json","vault.zip")
    upload = "Gated post with vault.zip attached"
  } -Force; $b
}

function Get-StockLane {
  $b = Get-ShipBase
  $b | Add-Member -NotePropertyMembers @{
    site = "stock"; fee = "CGTrader 15 to 40%; Etsy 6.5% plus 20c plus 3% plus 25c"; keep = "CGTrader 60 to 85% by level; Etsy about 90% less fees"
    price = 'CGTrader $14.99, Etsy $12.99'; aiTag = "CGTrader AI flag; Etsy designed-with-AI note"
    files = @("cgtrader-listing.txt","etsy-listing.txt","manifest.json","pack.zip","thumb.png")
    upload = "CGTrader and Etsy web upload of pack.zip"
  } -Force; $b
}

function Get-MinecraftLane {
  $b = Get-ShipBase
  $b | Add-Member -NotePropertyMembers @{
    site = "minecraft"; fee = "about 50%"; keep = "about 50%"
    price = "490 Minecoins"; aiTag = "Partner submit AI use note"
    files = @("minecraft-listing.txt","manifest.json","pack.mcpack","thumb.png")
    upload = "Minecraft Partner portal submit of pack.mcpack"
  } -Force; $b
}

function Get-UefnLane {
  $b = Get-ShipBase
  $b | Add-Member -NotePropertyMembers @{
    site = "uefn"; fee = "40% pool to creators by play; asset sales same as Fab 12%"; keep = "share of pool, not per sale"
    price = "Free island plus engagement pay"; aiTag = "UEFN publish Generative AI disclosure"
    files = @("uefn-listing.txt","manifest.json","island.zip")
    upload = "UEFN editor Publish to Fortnite"
  } -Force; $b
}

function Get-AllLanes {
  @((Get-FabLane),(Get-UnityLane),(Get-SlMarketLane),(Get-RobloxLane),(Get-ItchLane),(Get-VaultLane),(Get-StockLane),(Get-MinecraftLane),(Get-UefnLane))
}

function Write-ShipListings {
  param([string]$Out = "./out")
  New-Item -ItemType Directory -Force -Path $Out | Out-Null
  foreach ($lane in (Get-AllLanes)) {
    $p = Join-Path $Out ($lane.site + "-listing.txt")
    Get-ShipListingText $lane | Out-File -Encoding utf8 $p
  }
  Get-AllLanes | ConvertTo-Json -Depth 4 | Out-File -Encoding utf8 (Join-Path $Out "manifest.json")
}
