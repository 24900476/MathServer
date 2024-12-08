# Ex.05 Design a Website for Server Side Processing
## Date:08.12.2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html
<!DOCTYPE html>
<html lang="en">
<head >
<meta charset="UTF-8">
<title>javascript</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    input{
        border: radius 10px;
        padding: 10px;
        margin-top: 10px;
        margin-right: 5px;
        }
        body{
            margin-top: 15%;
            }
        h1{
            color:rgb(116, 8, 69);
            font-size:40pz;
            }
        form{
            background-color:#1abaa5; 
            
            width: 450px; ;
            }
</style>
<script>
    function pow(){
        var x=document.getElementById("a").value
        var y=document.getElementById("b").value
        document.getElementById('r').innerText="Power:" +x*x*y
        }
</script>
</head>
<body>
    <H2>
        <br>
        <center>
            <form>
                <h1>Power Calculator</h1>
                <input type="text" placeholder="Enter intensity" id="a"><br>
                <input type="text" placeholder="Enter resistance" id="b"><br>
                <input type="button" value="calculate" onclick="pow()"><br>
                <label id="r"></label>
            </form>
        </center>
    </H2>
</body>


views.py

from django.shortcuts import render
def EnergyCalc(request):
    context = {
        'power' : "0",
        'intensity' : "0",
        'resistance': "0"
    }
    if request.method == 'POST':
        print("POST method is used")
        intensity = request.POST.get('intensity', '0')
        resistance = request.POST.get('resistance', '0')
        print('Request=',request)
        print('Intensity(I) =',intensity)
        print('Resistance(R) =', resistance)
        try:
            intensity = float(intensity)
            resistance = float(resistance)
            power = intensity ** 2 * resistance

            context['power'] = round(power,2)
            context['intensity']=round(intensity,2)
            context['resistance']=round(resistance,2)
            print(f'Calculated Power:{power}')


        except ValueError as e:
           print(f'Error in calculation:{e}')
           context['power']="Invalid input.please enter valid numbers."
    return render(request, 'mathapp/math.html', context)


urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views 
urlpatterns = [
path('admin/', admin.site.urls), 
path('', views.EnergyCalc, name="EnergyCalc") # Root URL redirect
]


```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-12-08 224052.png>)


## HOMEPAGE:
![alt text](<Screenshot 2024-12-08 224010.png>)

## RESULT:
The program for performing server side processing is completed successfully.
