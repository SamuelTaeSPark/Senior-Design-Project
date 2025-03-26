import tkinter as tk

button_states = {}
# Initialize button states for 101-103
button_states[101] = 0
button_states[102] = 0
button_states[103] = 0

# ========================== Centralized Color System ==========================
# Button states dictionary (tracks the state of each button)
color_states = [
    ("black", "cyan"),  # 0
    ("black", "darkorange"),  # 1
    ("black", "green"),  # 2
    ("black", "gray"),  # 3
    ("black", "lightgreen"),  # 4
    ("black", "orange"),  # 5
    ("black", "red"),  # 6
    ("black", "white")]  # 7

color_keys = {
    "4_state": [3, 7, 4, 1],  # gray, white, lightgreen, darkorange
    "3_state": [3, 7, 4],  # Uses indexes from color_states (gray, white, lightgreen)
    "icon_3state_orange": [3, 5, 5],  # gray, orange, orange
    "icon_3state_red": [3, 2, 6],  # gray, green, red
    "icon_3state_green": [3, 2, 3],  # gray, green, gray
    "icon_state": [3, 7, 0]  # gray, white, cyan
}

default_fault_messages_text = "No Messages"

# ============= Global Variables =======================
fault_messages_text = default_fault_messages_text

speed_var = 0

v2x_switch_var = 0
lateral_switch_var = 0
longitudinal_switch_var = 0
V2X_Switch_text = "V2X Switch"
Lateral_Switch_text = "Lateral Switch Switch"
Longitudinal_Switch_text = "Longitudinal Switch Switch"


# =======================================================================

def toggle_button_state(button, button_id, color_key, fg_blink_color=None, physical_button_press=None):
    """Generalized function to toggle button states using color indexes."""
    current_state = button_states[button_id]

    # Get the color scheme and state count from color_key
    color_indexes = color_keys.get(color_key, color_keys["3_state"])  # Default to 3_state if not found
    state_count = len(color_indexes)

    if physical_button_press == 1 and button_id == 4:
        if current_state == 1:
            current_state = 1
        else:
            current_state = (current_state - 1) % state_count
    if physical_button_press == 1 and (button_id == 0 or button_id ==  3):
        #print("in physical button press: ",current_state)
        if current_state == 0:
            current_state = 0
        else:
            current_state = (current_state - 1) % state_count

    new_state = (current_state + 1) % state_count  # Go through states
    #print(new_state)

    bg_color, fg_color = color_states[color_indexes[new_state]]  # Get colors using index

    # Apply new colors
    button.config(bg=bg_color, fg=fg_color)

    # Update state
    button_states[button_id] = new_state

    # Handle blinking for certain states
    if state_count == 4 and new_state == 3 and button_id > 25:  # Blinking for 4-state icons
        blink_button(button, button_id, fg_blink_color)
    elif state_count == 3 and new_state == 2 and button_id > 25:  # Blinking for 3-state icons
        blink_button(button, button_id, fg_blink_color)


def add_toggle_button(frame, text, button_id, color_key="3_state", fg_blink_color=None,
                      button_press=None, grid=None, row=0, col=0, text_box=None,ain_button=None,lcc_button=None):
    """Create toggle buttons using the color system."""
    color_indexes = color_keys.get(color_key, color_keys["3_state"])  # Default to 3_state
    bg_color, fg_color = color_states[color_indexes[0]]  # Initial state colors

    if grid:
        button = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 16, "bold"), bg=bg_color, fg=fg_color,
                           activebackground="gray", command=lambda: toggle_button_state(button, button_id, color_key,
                                                                                        fg_blink_color, button_press))
    else:
        '''button = tk.Button(frame, text=text, borderwidth=10, highlightthickness=0, width=8, height=4,font=("Arial", 12),
                           bg=bg_color, fg=fg_color, activebackground="gray", activeforeground="black",
                           command=lambda: toggle_button_state(button, button_id, color_key))'''
        button = tk.Button(frame, text=text, borderwidth=10, highlightthickness=0, width=8, height=4,
                           font=("Arial", 12),
                           bg=bg_color, fg=fg_color, activebackground="gray", activeforeground="black",
                           command=lambda: check_if_button_can_do_something(button, button_id, color_key, text_box=text_box,
                                                                            ain_button=ain_button,lcc_button=lcc_button))

    # Place in grid if specified, else use pack()
    if grid:
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        button.pack(pady=5)

    # Initialize button state
    button_states[button_id] = 0
    return button

def check_if_button_can_do_something(button, button_id, color_key, fg_blink_color=None, button_press=None, text_box=None,
                                     ain_button=None,lcc_button=None):
    # AIN, (automatic intersection navigation) check: v2x, ACC, & speed < 35
    if button_id == 0:
        print("in ACC button_id")
        fault_messages_text = default_fault_messages_text

        toggle_button_state(button, button_id, fg_blink_color,button_press)
    # DMS, (driver monitoring system), check:
    elif button_id == 1:
        print("in ACC button_id")
        fault_messages_text = default_fault_messages_text

        toggle_button_state(button, button_id, fg_blink_color)
    # DYNO, check: ??
    elif button_id == 2:
        print("in ACC button_id")
        fault_messages_text = default_fault_messages_text

        toggle_button_state(button, button_id, fg_blink_color)
    # LCC, (lane centering control) check: lateral switch, ACC, lane detected, speed < 35, centered in lane
    elif button_id == 3:
        print("in LCC button_id")
        fault_messages_text = default_fault_messages_text
        if lateral_switch_var and button_states[4] == 2 and speed_var < 35:
            print("passed LCC condition check")
            # toggle if lateral switch, ACC, lane detected, speed < 35
            if button_states[button_id] == 1:
                #print("LCC ON: ", button_id, "\n", button_states[button_id])
                print("LCC ON")
                toggle_button_state(button, button_id, color_key)
            else:
                print("LCC Standby")
                button_states[button_id] = 0
                toggle_button_state(button, button_id, color_key)
        else:
            print("failed LCC condition check")
            fault_messages_text="Cannot Enable LCC.\nLateral Switch and ACC not ON\nSpeed must be < 35"
            button_states[button_id] = 2
            toggle_button_state(button, button_id, color_key)

        if text_box:
            text_box.config(state="normal")
            text_box.delete("1.0", tk.END)
            text_box.insert("1.0", fault_messages_text)
            text_box.config(state="disabled")
    # ACC/CACC, (Adaptive Cruise Control/Eco-Cooperative Adaptive Cruise), check: longitudinal & v2x switch, ACC button press
    elif button_id == 4:
        # first test with toggle logic
        print("in ACC button_id")
        fault_messages_text = default_fault_messages_text
        if button_states[button_id] == 0:
            print("in ACC State Check")
            # toggle if Long & v2x
            if v2x_switch_var and longitudinal_switch_var:
                print("passed ACC condition check")
                toggle_button_state(button, button_id, color_key)
            else:
                print("failed ACC condition check")
                fault_messages_text="Cannot Enable ACC/CACC.\nV2X and Longitudinal Switch\nnot ON"
        else:
            print("ACC OFF")
            button_states[button_id] = 2
            toggle_button_state(button, button_id, color_key)
            button_states[0] = 2
            toggle_button_state(ain_button, 0, color_key)
            button_states[3] = 2
            toggle_button_state(lcc_button, 3, color_key)
            
        # update text box
        if text_box:
            text_box.config(state="normal")
            text_box.delete("1.0", tk.END)
            text_box.insert("1.0", fault_messages_text)
            text_box.config(state="disabled")
        '''#toggling buttons
        toggle_4_button_grid(button, button_id, fg_blink_color,button_press)'''

def blink_button(button, button_id, fg_blink_color):
    """Makes the button blink when in active state."""
    if button_states[button_id] in [2, 3]:  # Active states that should blink
        current_fg = button.cget("fg")
        new_fg = fg_blink_color if current_fg == "gray" else "gray"
        button.config(fg=new_fg)
        button.after(500, lambda: blink_button(button, button_id, fg_blink_color))


def on_switch_print(button_id, button):
    """Toggle text color of the switches."""
    global v2x_switch_var
    global lateral_switch_var
    global longitudinal_switch_var

    button_states[button_id] = not button_states[button_id]
    button.config(fg="lightgreen") if button_states[button_id] else button.config(fg="gray")

    # Track V2X Switch ON/OFF
    if button_id == 101:
        if v2x_switch_var != button_states[button_id]:
            v2x_switch_var = button_states[button_id]
        print("V2X Switch Toggled: ", v2x_switch_var)

    # Track Lateral Switch ON/OFF
    if button_id == 102:
        if lateral_switch_var != button_states[button_id]:
            lateral_switch_var = button_states[button_id]
        print("Lateral Switch Toggled: ", lateral_switch_var)

    # Track Longitudinal Switch ON/OFF
    if button_id == 103:
        if longitudinal_switch_var != button_states[button_id]:
            longitudinal_switch_var = button_states[button_id]
        print("Longitudinal Switch Toggled: ", longitudinal_switch_var)

def speed_change(speed, sign, display):
    global speed_var
    """Handle speed changes."""
    speed.set(speed.get() + int(sign))
    display.set(f"{speed.get()} mi/h")
    if speed.get() != speed_var:
        speed_var = speed.get()


def main():
    HMI_Window = tk.Tk()
    HMI_Window.title("HMI Example")
    HMI_Window.geometry("1080x720")

    driving_mode_text = "Driver Mode: Eco"
    CACC_messages_text = "Gap:\n-- m\n Headway:\n-- Sec\nCACC Mileage:\n--mi"

    # Create a PanedWindow to split the window into two resizable sections
    paned_window = tk.PanedWindow(HMI_Window, orient=tk.HORIZONTAL)
    paned_window.pack(fill=tk.BOTH, expand=True)

    # Left side: Scrollable frame for buttons
    left_frame = tk.Frame(paned_window, width=100)
    paned_window.add(left_frame, minsize=100)

    canvas = tk.Canvas(left_frame, width=100)
    scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=canvas.yview, width=10)
    scrollable_frame = tk.Frame(canvas, width=100, bg="black")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set, bg="black")

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    
    # Middle frame with grid of icons
    middle_frame = tk.Frame(paned_window, bg="black")
    paned_window.add(middle_frame)

    text_box = tk.Text(middle_frame, height=3, width=25, font=("Arial", 24), bg="white", fg="red",
                       highlightbackground="red", highlightcolor="red", highlightthickness=10)
    text_box.pack(side="top", fill="x", padx=10, pady=5)
    text_box.insert("1.0", fault_messages_text)
    text_box.config(state="normal")  # makes it read only

    grid_container = tk.Frame(middle_frame, bg="black")
    grid_container.pack(side="top", expand=False, pady=10)

    for i in range(5):
        grid_container.columnconfigure(i, weight=1)

    # Add buttons to the scrollable frame
    ain_button = add_toggle_button(scrollable_frame, "AIN", 0, "3_state", text_box=text_box)
    dms_button = add_toggle_button(scrollable_frame, "DMS", 1, "3_state", text_box=text_box)
    dyno_button = add_toggle_button(scrollable_frame, "DYNO", 2, "3_state", text_box=text_box)
    lcc_button = add_toggle_button(scrollable_frame, "LCC", 3, "3_state", text_box=text_box)
    acc_button = add_toggle_button(scrollable_frame, "ACC", 4, "3_state", text_box=text_box,
                                   ain_button=ain_button,lcc_button=lcc_button)

    # Add icon buttons
    add_toggle_button(grid_container, "MIL\nIcon", 50, "icon_3state_orange",
                      "darkorange", None,1,0 ,0 )
    add_toggle_button(grid_container, "Vehicle\nAhead\nIcon",51, "icon_3state_red",
                      "red", None, 1, 0,1)
    add_toggle_button(grid_container, "ACC\nIcon", 52, "4_state", "darkorange",
                      None, 1, 0,2)
    add_toggle_button(grid_container, "AIN\nIcon", 53, "4_state", "darkorange",
                      None,1, 0,3)
    add_toggle_button(grid_container, "DMS\nIcon", 54, "icon_3state_green",
                      "darkorange", None,1, 0, 4)

    add_toggle_button(grid_container, "Battery\nHeat\nIcon", 55, "icon_3state_red",
                      "red", None, 1, 1, 0)
    add_toggle_button(grid_container, "PCM\nHeat\nIcon", 56, "icon_3state_red", "red",
                      None,1, 1, 1)
    add_toggle_button(grid_container, "V2X\nIcon", 57, "icon_3state_green", "green",
                      None,1, 1, 2)
    add_toggle_button(grid_container, "Long\nControl\nIcon", 58, "icon_3state_green",
                      "green", None,1, 1, 3)
    add_toggle_button(grid_container, "Lat\nControl\nIcon", 59, "icon_3state_green",
                      "green", None,1, 1, 4)

    add_toggle_button(grid_container, "UDP\nIcon", 60, "icon_3state_orange",
                      "darkorange", None,1, 2, 0)
    add_toggle_button(grid_container, "DYNO\nREQ\nIcon", 61, "icon_state", "white",
                      None,1, 2, 1)
    add_toggle_button(grid_container, "SIM\nOBJ\nIcon", 62, "icon_state", "white",
                      None,1, 2, 2)
    add_toggle_button(grid_container, "LCC\nIcon", 63, "4_state", "darkorange",
                      None,1, 2, 3)

    # Add text displays
    text_box2 = tk.Text(middle_frame, height=1, width=25, font=("Times New Roman", 24), bg="black", fg="white",
                        highlightbackground="gray", highlightcolor="black", highlightthickness=3)
    text_box2.place(relx=0.5, rely=0.55, anchor="n")
    text_box2.tag_configure("center", justify="center")
    text_box2.insert("1.0", driving_mode_text)
    text_box2.config(state="normal")

    text_box3 = tk.Text(middle_frame, height=6, width=25, font=("Times New Roman", 24), bg="black", fg="white",
                        highlightbackground="gray", highlightcolor="white", highlightthickness=10)
    text_box3.place(relx=0.5, rely=0.65, anchor="n")
    text_box3.tag_configure("center", justify="center")
    text_box3.insert("1.0", CACC_messages_text)
    text_box3.config(state="normal")

    # ================================== future project ==================================
    # Right: Add other content here
    right_frame = tk.Frame(paned_window, bg="gray")
    paned_window.add(right_frame, stretch="always")
    # ================================== future project ==================================

    # New Window for switches and speed controls
    Non_HMI_Window = tk.Toplevel(HMI_Window, bg="black")
    Non_HMI_Window.title("Switches and Speed")

    switch_frame = tk.Frame(Non_HMI_Window, bg="black")
    switch_frame.grid(row=1, column=0, columnspan=3, pady=5)
    
    # physical switches
    v2xSwitch = tk.Checkbutton(switch_frame, text=V2X_Switch_text, variable=v2x_switch_var,
                               onvalue=1, offvalue=0, bg="black", fg="gray", relief="raised",
                               command=lambda: on_switch_print(101, v2xSwitch))
    v2xSwitch.grid(row=0, column=0, padx=5)

    lateralSwitch = tk.Checkbutton(switch_frame, text=Lateral_Switch_text, variable=lateral_switch_var,
                                   onvalue=3, offvalue=2, command=lambda: on_switch_print(102, lateralSwitch),
                                   bg="black", fg="gray", relief="raised")
    lateralSwitch.grid(row=0, column=1, padx=5)

    longitudinalSwitch = tk.Checkbutton(switch_frame, text=Longitudinal_Switch_text, variable=longitudinal_switch_var,
                                        command=lambda: on_switch_print(103, longitudinalSwitch),
                                        bg="black", fg="gray", relief="raised", onvalue=5, offvalue=4)
    longitudinalSwitch.grid(row=0, column=2, padx=5)

    # Speed control
    speed_frame = tk.Frame(Non_HMI_Window, bg="black")
    speed_frame.grid(row=2, column=0, columnspan=3, pady=10)

    speed_val = tk.IntVar(value=0)
    speed_display = tk.StringVar(value="0 mi/h")

    decrement_speed = tk.Button(speed_frame, text="-", width=2,
                                command=lambda: speed_change(speed_val, -1, speed_display),
                                bg="black", fg="gray", relief="raised")
    decrement_speed.grid(row=0, column=0, padx=5, pady=5)

    speed_label = tk.Label(speed_frame, textvariable=speed_display, bg="black", fg="white", font=("Arial", 16))
    speed_label.grid(row=0, column=1, padx=5, pady=5)

    increment_speed = tk.Button(speed_frame, text="+", width=2,
                                command=lambda: speed_change(speed_val, 1, speed_display),
                                bg="black", fg="gray", relief="raised")
    increment_speed.grid(row=0, column=2, padx=5, pady=5)

    set_and_res_frame = tk.Frame(Non_HMI_Window, bg="black")
    set_and_res_frame.grid(row=4, column=0, columnspan=3, pady=10)

    set_speed_button = tk.Button(set_and_res_frame, text="SET-", borderwidth=10, highlightthickness=0, width=6,
                                 height=1, font=("Arial", 12), bg="black", fg="white", activebackground="gray",
                                 activeforeground="black",
                                 command=lambda: [
                                     toggle_button_state(acc_button, 4, "3_state",physical_button_press=1),
                                     toggle_button_state(lcc_button, 3, "3_state",physical_button_press=1),
                                     toggle_button_state(ain_button, 0, "3_state",physical_button_press=1),
                                 ])
    set_speed_button.grid(row=0, column=0, padx=5, pady=5)

    reset_speed_button = tk.Button(set_and_res_frame, text="RES+", borderwidth=10, highlightthickness=0, width=6,
                                   height=1, font=("Arial", 12), bg="black", fg="white", activebackground="gray",
                                   activeforeground="black")
    reset_speed_button.grid(row=0, column=2, padx=5, pady=5)

    # Centering the frames in the window
    Non_HMI_Window.grid_columnconfigure(0, weight=1)
    Non_HMI_Window.grid_columnconfigure(1, weight=1)
    Non_HMI_Window.grid_columnconfigure(2, weight=1)

    HMI_Window.mainloop()


if __name__ == "__main__":
    main()
