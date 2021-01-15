# Variables
$resourceGroup = "Challenge8RecourceGroup"
$securityGroup = "Challenge8SecurityGroup"
$location = "westeurope"

# VM Names
$iisVMname = "WEB01"
$wsName = "WS01"


# Get credentials
$cred = Get-Credential -Message "Enter a username and password, these will be used as the credentials for the VM's."


# Security Rules
# HTTP Rule
$httprule = New-AzNetworkSecurityRuleConfig `
    -Name "HTTP_Rule" `
    -Description "Allow HTTP" `
    -Access "Allow" `
    -Protocol "Tcp" `
    -Direction "Inbound" `
    -Priority "101" `
    -SourceAddressPrefix * `
    -SourcePortRange * `
    -DestinationAddressPrefix * `
    -DestinationPortRange 80
# RDP Rule
$rdprule = New-AzNetworkSecurityRuleConfig `
    -Name "RDP_Rule" `
    -Description "Allow RDP" `
    -Access "Allow" `
    -Protocol "Tcp" `
    -Direction "Inbound" `
    -Priority "100" `
    -SourceAddressPrefix * `
    -SourcePortRange * `
    -DestinationAddressPrefix * `
    -DestinationPortRange 3389


# Create Resource Group
New-AzResourceGroup -Name $resourceGroup -Location $location


# Create Security Group
New-AzNetworkSecurityGroup `
  -Name $securityGroup `
  -ResourceGroupName $resourceGroup `
  -Location $location `
  -SecurityRules $httprule,$rdprule


# Create Windows 10 VM
New-AzVM `
  -ResourceGroupName $resourceGroup `
  -Name $wsName `
  -Location $location `
  -ImageName "MicrosoftWindowsDesktop:Windows-10:20h1-pro:19041.508.2009070256" `
  -VirtualNetworkName "Challenge8Network" `
  -SubnetName "Challenge8Subnet" `
  -SecurityGroupName $securityGroup `
  -Credential $cred


# Create Windows Server VM
New-AzVM `
  -ResourceGroupName $resourceGroup `
  -Name $iisVMname `
  -Location $location `
  -ImageName "Win2019Datacenter" `
  -VirtualNetworkName "Challenge8Network" `
  -SubnetName "Challenge8Subnet" `
  -SecurityGroupName $securityGroup `
  -PublicIpAddressName "Challenge8Publicip" `
  -Credential $cred


# Install IIS
$PublicSettings = '{"commandToExecute":"powershell Add-WindowsFeature Web-Server"}'

Set-AzVMExtension -ExtensionName "IIS" -ResourceGroupName $resourceGroup -VMName $iisVMname `
  -Publisher "Microsoft.Compute" -ExtensionType "CustomScriptExtension" -TypeHandlerVersion 1.4 `
  -SettingString $PublicSettings -Location $location
