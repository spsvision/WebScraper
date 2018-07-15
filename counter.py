import requests
import csv
from bs4 import BeautifulSoup

total_count = 0

f = csv.writer(open('sketchfab.csv', 'w'))
f.writerow(['Name', 'Downloads'])

pages = ["https://sketchfab.com/models/4e15331cc9cc4234b4b19ab39da7f5d9",
"https://sketchfab.com/models/92a0dff160b2413ebeb2e91b1899b998",
"https://sketchfab.com/models/685ca14d035347dd91c79b19c34a1a8e",
"https://sketchfab.com/models/716a6a9018ab4a249fd35a7b3014fca3",
"https://sketchfab.com/models/f06caa7a30004045861594c2169f9cc9",
"https://sketchfab.com/models/5b67ab9da2cd4acf9a5c1537945f2960",
"https://sketchfab.com/models/c048f623b8de490c9e66a2b5270480fc",
"https://sketchfab.com/models/2f9e5079b3f34db3a961e149ee787718",
"https://sketchfab.com/models/3b7b7e65a8e94d7ab8c85a40d3d5abd4",
"https://sketchfab.com/models/7ce04b7410a9481b8d03f40915e7ff7f",
"https://sketchfab.com/models/cdad48f8534d4aba895816ace0e50625",
"https://sketchfab.com/models/97be0c16fea94075b17190be8e6bb2e4",
"https://sketchfab.com/models/f779b7214bda4e06869f9d83e9dae8d7",
"https://sketchfab.com/models/d45daf23045b46879d43a81aa1bb02df",
"https://sketchfab.com/models/d9fdb2332173441b8dc6735c56d5370f",
"https://sketchfab.com/models/21d360d69acf438dbbaadef1b85e780e",
"https://sketchfab.com/models/c221a57c8b624c51ab6d0e953e36f879",
"https://sketchfab.com/models/5aef59e2f4484a42ac66ffb500a7be7b",
"https://sketchfab.com/models/e63a874fa2654ee3a181f23a1a7502e9",
"https://sketchfab.com/models/6ec8b6d1a924455bbb7e3e3e55827b2d",
"https://sketchfab.com/models/8bb6854e3ded4dda82da4517d8fc661b",
"https://sketchfab.com/models/1caee43cf76049dfa4c6369dc7df3cd5",
"https://sketchfab.com/models/72592399420e4bf5a01be5a0c08d30ef",
"https://sketchfab.com/models/6fb416e2e7b245888530d1ac145e297f",
"https://sketchfab.com/models/2506901ceb6942bcaf66fe2f802a6b7e",
"https://sketchfab.com/models/be3ec583c6004241a1bac1b366e5e953",
"https://sketchfab.com/models/60912bb53b4f479db51c55e53d03d6be",
"https://sketchfab.com/models/9d3643df00be4de78c247ca552068cdb",
"https://sketchfab.com/models/04c2af46fcba4932839d0e4ddca5b1a1",
"https://sketchfab.com/models/fa812f931a8c4c438a6de945e1eb5ec5",
"https://sketchfab.com/models/4668c317df3e4d13996d20d97cae8085",
"https://sketchfab.com/models/1a410659922c4f25be1ec427b969a4b9",
"https://sketchfab.com/models/a08e37707031419b9abbaa3e2159f245",
"https://sketchfab.com/models/f1ea98e106b24b1c81a5a0af7c866d62",
"https://sketchfab.com/models/a3b5ec6302f24bcfaab232fc10d21b5e",
"https://sketchfab.com/models/aff7dd10461b4c9da14271853ad584f1",
"https://sketchfab.com/models/9a7d317fea29496ba0b2c5cd83be473f",
"https://sketchfab.com/models/dcc9ecfc0b1a4240b614cb01a07d2553",
"https://sketchfab.com/models/60dec74c203b448ea6ffddbd84fac36f"]

sketchfab_count = 0

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    name = soup.find("span", class_="model-name__label").get_text()
    d_help = soup.find(class_="downloads help")
    d_tool = d_help.find(class_="tooltip tooltip-down")
    count = d_tool.find(class_="count").get_text()
    sketchfab_count += int(count)
    #print(name+" has been downloaded "+count + " times.")
    f.writerow([name, count])
    
pages = ["https://3dwarehouse.sketchup.com/model/u98990ede-c350-4ba7-870e-2f9db8c2d840/Vision-Park","https://3dwarehouse.sketchup.com/model/u9f922ab3-3f26-4cbb-85f6-2f5f080f9079/SolarWindRain-All-in-one-Energy-Generator",
"https://3dwarehouse.sketchup.com/model/ua2f3b650-7af7-4995-bf4a-e9037752c25a/McKenzie-Avenue-Highway-1-Interchange",
"https://3dwarehouse.sketchup.com/model/u36f4077b-ca2c-42d0-a033-4611a86ac4f7/Moving-Tidal-Energy",
"https://3dwarehouse.sketchup.com/model/u3d49b955-a1bf-44f4-97eb-d390c754ccbf/Regenerative-Seabus",
"https://3dwarehouse.sketchup.com/model/ucaf60222-81e1-4551-9046-21abe5a6b3e0/SPS-Charging-Station",
"https://3dwarehouse.sketchup.com/model/u76877beb-86b7-47ea-9e8c-d046676a5893/DAC-Dynamic-Assistance-Cart",
"https://3dwarehouse.sketchup.com/model/ub4d9c70e-26be-40c0-9ddf-69e20a08a53f/Lions-Gate-Bridge-Multi-Level-Initiative",
"https://3dwarehouse.sketchup.com/model/u7bab488e-45ab-474e-a853-4ad632cf4bca/Basic-IKEA-Model",
"https://3dwarehouse.sketchup.com/model/dcbe82b8-6f8b-4fef-b78d-513420f97b2b/Speed-Trap-Intersection",
"https://3dwarehouse.sketchup.com/model/ub699dba9-d67c-4dda-a681-869e4fe2df84/Piezoelectric-Weather-Panels",
"https://3dwarehouse.sketchup.com/model/uef27b0b6-2297-4a04-aab5-3c5053dd5a50/Breeze-Generator",
"https://3dwarehouse.sketchup.com/model/77c709c4-013f-4c7a-904b-718749d8cf45/Thermionic-Road-Converters",
"https://3dwarehouse.sketchup.com/model/u67441100-1632-4dd8-a07f-2c27065ba6c2/Google-Maps-Kiosk",
"https://3dwarehouse.sketchup.com/model/3eca54dc-7ed0-417a-9ed1-2eaf883a02f8/WheelChair-Lift",
"https://3dwarehouse.sketchup.com/model/b35be6d7-b45d-459e-8b1d-65ce070ed746/Moving-Overhead-Walkway",
"https://3dwarehouse.sketchup.com/model/1d6a1344-8ba8-4d71-9055-ffa7b7ce6769/Collector-Bale",
"https://3dwarehouse.sketchup.com/model/1adbd85a-2232-4e3a-a383-658a9895b58e/Mechanical-Feed",
"https://3dwarehouse.sketchup.com/model/52292370-10ce-4afa-87ef-86ea1e5fc62f/Tertiary-Boiler",
"https://3dwarehouse.sketchup.com/model/9fe4950e-9079-487f-b4e2-20603f708e75/OP-S200",
"https://3dwarehouse.sketchup.com/model/a08af6ad-2c64-4fb1-8628-131e9b478caa/Airbus-A350-Winglet",
"https://3dwarehouse.sketchup.com/model/5c6d691d-70e2-40d9-a5ad-d365828267d1/Propeller",
"https://3dwarehouse.sketchup.com/model/0739de39-da44-4735-9138-4d47e84eff83/SPS-Aquila-Solar-Airplane",
"https://3dwarehouse.sketchup.com/model/1e4615d4-968f-4675-83f5-f574d9e53a03/Spherical-Underwater-Autonomous-Vehicle",
"https://3dwarehouse.sketchup.com/model/c9a293f4-f4a1-46c7-8126-c11949056c55/Multi-Directional-Hyperloop",
"https://3dwarehouse.sketchup.com/model/d72145dd-4abb-4e7f-ba46-c12dc1e74c69/Multi-directional-Hyperloop-Tracks",
"https://3dwarehouse.sketchup.com/model/881477f4-9eab-4df5-b8f7-2605e35f8ba4/Hyperloop-Pod",
"https://3dwarehouse.sketchup.com/model/0bf0a113-580f-4d04-8d45-9744a9d97367/Solar-Rain-Energy-Capturing-Device",
"https://3dwarehouse.sketchup.com/model/cbda433b-baa1-4aba-96cf-4634ae824c71/Boiler-Pipe-System",
"https://3dwarehouse.sketchup.com/model/50767def-fa5a-4906-9e97-b3559fa26c5b/Two-Level-Pipe-Boiler-System",
"https://3dwarehouse.sketchup.com/model/5f90557c-c32f-4b2a-8dc7-db97ed16ecec/Modern-Day-Sewage-Plant",
"https://3dwarehouse.sketchup.com/model/2a59f77b-3cde-4700-8700-e85b62b6f1e8/AIrbus-A350-XWB",
"https://3dwarehouse.sketchup.com/model/7254e85f-cebc-4571-8805-b5b75caa4f42/DJI-M100",
"https://3dwarehouse.sketchup.com/model/6f088c69-942a-437a-a51b-acfc1108adc4/Piezoelectric-Weather-Panel-V2",
"https://3dwarehouse.sketchup.com/model/2a66f280-3e3f-42cc-be5e-4cdc5e85f902/Aircraft-Engine",
"https://3dwarehouse.sketchup.com/model/u5494fb08-fdbd-42ab-82b7-01a5b2f26b8b/McKenzie-Interchange-Victoria-BC",
"https://3dwarehouse.sketchup.com/model/9c4cbd2d-30a3-41d7-88a6-d675e290afa9/Fraser-River-Skytrain-Bridge",
"https://3dwarehouse.sketchup.com/model/c05ab2f6-f0e5-45a2-8cb3-7794267c4cb5/Generic-SPS-Jeep",
"https://3dwarehouse.sketchup.com/model/e318b7b1-b2f9-4147-b665-86fb513ce16c/Steering-Wheel",
"https://3dwarehouse.sketchup.com/model/5eecfdac-b6fd-4017-a6d1-319e1667241b/Standard-Wheel",
"https://3dwarehouse.sketchup.com/model/d87767a6-c3f2-4ced-b085-c33d5a9ffb08/Powerwall-2",
"https://3dwarehouse.sketchup.com/model/78e149eb-d9e9-4c4e-af5e-2f52ca19a463/Battery-Pack-Radiator"]
f = csv.writer(open('3Dsketchware.csv', 'w'))
f.writerow(['Name', 'Downloads'])
dwarehouse_count = 0
for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    name_div = soup.find("div", id="model-title-banner")
    name = name_div.find("h1").get_text()
    count = soup.find(class_="downloadsCount").get_text()
    counter = count.replace("Downloads","")
    counter2 = counter.replace("K","000")
    count = counter2
    dwarehouse_count += int(count)
    #print(name+" has been downloaded "+count + " times.")
   

# Grabcad counter
page = requests.get("https://grabcad.com/steven.samuel-1")
soup = BeautifulSoup(page.text, 'html.parser')
name_div = soup.find("table", class_="sidebar__table sidebar__table--alt")
di = name_div.find_all('tr')[1]
down = di.find('td')
grabcad_count = int(down.get_text())

total_count = sketchfab_count + dwarehouse_count + grabcad_count

print("Total Downloads:\n Sketchfab: "+ str(sketchfab_count) + " 3D Warehouse: " + str(dwarehouse_count) + " Grabcad: " +str(grabcad_count))
print("Overall, your models have been downloaded "+ str(total_count) + " times")
    
