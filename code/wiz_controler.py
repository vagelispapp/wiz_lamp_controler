import asyncio

from pywizlight import wizlight, PilotBuilder

import customtkinter as ctk

settings = {'state':0, 'floor':0, 'desk':0, 'brightness':87}

def close(app):
    app.destroy()

def light_on(app):
    global settings     
    settings['state'] = 1
    close(app)

def light_off(app):
    global settings 
    settings['state'] = 0
    close(app)

# add or remove as many lamps you want
def floor_lamp():
    global settings
    # update settings 
    settings['floor'] = 1

# add or remove as many lamps you want 
def desk_lamp():
    global settings 
    # update settings 
    settings['desk'] = 1
    
def brightness(value):
    global settings   
    settings['brightness'] = value
    
async def main():
    global settings
    
    # set your light's ip
    light_floor = wizlight("192.168.1.X")
    light_desk= wizlight("192.168.1.X")
        
    if settings['state']:
        await light_desk.turn_on(PilotBuilder(brightness = settings['brightness']))
        if settings['floor']:
            await light_floor.turn_on(PilotBuilder(brightness = settings['brightness']))
            
    else:
        await light_floor.turn_off()
        if settings['desk']:
            await light_desk.turn_off()

def gui():
    app = ctk.CTk()
    app.geometry("400x250")
    
    upper_frame = ctk.CTkFrame(app, fg_color='transparent')
    upper_frame.pack(pady=20)
    
    check_frame = ctk.CTkFrame(upper_frame, fg_color='transparent')
    check_frame.pack(padx=20, side='left')
    
    check_light1 = ctk.CTkCheckBox(check_frame, text='Floor Lamp', command=floor_lamp)
    check_light1.pack(pady=5)

    check_light2 = ctk.CTkCheckBox(check_frame, text='Desk Lamp', command=desk_lamp)
    check_light2.pack(pady=5)

    slider_frame = ctk.CTkFrame(upper_frame, fg_color='transparent')
    slider_frame.pack(padx=20, side='left')
    
    slider = ctk.CTkSlider(slider_frame, from_=0, to=255, command=brightness, orientation='vertical', height=80)
    slider.pack(pady=10)
    
    slider.set(87)

    button_frame = ctk.CTkFrame(app, fg_color='transparent')
    button_frame.pack(pady=20)

    button_on = ctk.CTkButton(button_frame, text="ON", command=lambda: light_on(app))
    button_on.pack(side='left', padx=10)

    button_off = ctk.CTkButton(button_frame, text="OFF", command=lambda: light_off(app))
    button_off.pack(side='left', padx=10)
    
    app.mainloop()

gui()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())