import tkinter as tk


button_states = {}

# Define color states
colors_4_state = [("black", "gray"), # State 0: Black background, gray text
                  ("black", "white"), # State 1: black background, white text
                  ("black", "lightgreen"), # State 2: black background, cyan text
                  ("black", "darkorange")] # State 2: black background, cyan text

# Define color states
colors_3_state = [("black", "gray"), # State 0: Black background, gray text
                  ("black", "white"), # State 1: black background, white text
                  ("black", "lightgreen")] # State 2: black background, cyan text

colors_icon_3state_orange = [("black", "gray"), # State 0: Black background, gray text
                     ("black", "orange"), # State 1: black background, white text
                     ("black", "orange")] # State 2: black background, cyan text
colors_icon_3state_red = [("black", "gray"), # State 0: Black background, gray text
                     ("black", "green"), # State 1: black background, white text
                     ("black", "red")] # State 2: black background, cyan text
colors_icon_3state_green = [("black", "gray"), # State 0: Black background, gray text
                     ("black", "green"), # State 1: black background, white text
                     ("black", "gray")] # State 2: black background, cyan text
colors_icon_state_ = [("black", "gray"), # State 0: Black background, gray text
                     ("black", "white"), # State 1: black background, white text
                     ("black", "cyan")] # State 2: black background, cyan text

def toggle_button_state(button, button_id, state_count, color_key, fg_blink_color=None, button_press=None):
    """Generalized function to toggle button states using color indexes."""
    current_state = button_states[button_id]
    new_state = (current_state + 1) % state_count  # Cycle through states

    # Get the color scheme dynamically from indexes
    color_indexes = color_keys.get(color_key, color_keys["3_state"])  # Default to 3_state if not found
    bg_color, fg_color = color_states[color_indexes[new_state]]  # Fetch colors using index

    # Apply new colors
    button.config(bg=bg_color, fg=fg_color)

    # Update state
    button_states[button_id] = new_state

    # Handle blinking for certain states
    if state_count == 4 and new_state == 3:  # Blinking for 4-state buttons
        blink_button(button, button_id, fg_blink_color)
    elif state_count == 3 and new_state == 2:  # Blinking for 3-state buttons
        blink_button(button, button_id, fg_blink_color)

    # Acknowledge button press if applicable
    if button_press is not None:
        button_press.set(1 if button_press.get() == 0 else 0)


def add_toggle_button(frame, text, button_id, state_count=3, color_key="3_state", fg_blink_color=None,
                      button_press=None, grid=None, row=0, col=0):
    """Generalized function to create toggle buttons dynamically selecting color indexes."""
    color_indexes = color_keys.get(color_key, color_keys["3_state"])  # Default to 3_state
    bg_color, fg_color = color_states[color_indexes[0]]  # Initial state colors

    button = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 16, "bold"),
                       bg=bg_color, fg=fg_color, activebackground="gray",
                       command=lambda: toggle_button_state(button, button_id, state_count, color_key, fg_blink_color,
                                                           button_press))

    # Place in grid if specified, else use pack()
    if grid:
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        button.pack(pady=5)

    # Initialize button state
    button_states[button_id] = 0


def add_button_text(frame, text_stuff, button_width, button_height):
    button = tk.Button(frame, text=text_stuff, borderwidth=10, highlightthickness=0,width=button_width, height=button_height
                       , font=("Arial", 12),bg="black", fg="white",activebackground="gray",activeforeground="black")
    button.pack(pady=5)
def add_button_image(frame, img_stuff):
    button = tk.Button(frame, image=img_stuff, borderwidth=10, highlightthickness=0)
    button.pack(pady=5)

def toggle_3_button(button, button_id):
    """Toggle button color and text between three states."""
    current_state = button_states[button_id]  # Get current state
    new_state = (current_state + 1) % 3  # Cycle between 0 → 1 → 2
    # Apply new colors
    button.config(bg=colors_3_state[new_state][0], fg=colors_3_state[new_state][1])
    # Update state in dictionary
    button_states[button_id] = new_state

def add_toggle_button(frame, text_stuff, button_id):
    """Create a toggle button with three color states."""
    button = tk.Button(frame, text=text_stuff, borderwidth = 10, highlightthickness = 0, width = 8, height = 4,
                       font = ( "Arial", 12), bg=colors_3_state[0][0], fg=colors_3_state[0][1], activebackground="gray",
                       activeforeground = "black",
                       command=lambda: toggle_3_button(button, button_id))
    button.pack(pady=5)
    # Initialize button state
    button_states[button_id] = 0


def toggle_3_button_grid(button, button_id, bg_blink_color):
    """Toggle button color and text between three states."""
    current_state = button_states[button_id]  # Get current state
    new_state = (current_state + 1) % 3  # Cycle between 0 → 1 → 2
    # Apply new colors
    if button_id == 50:
        button.config(bg=colors_icon_3state_orange[new_state][0], fg=colors_icon_3state_orange[new_state][1])
    elif button_id == 51:
        button.config(bg=colors_icon_3state_red[new_state][0], fg=colors_icon_3state_red[new_state][1])
    elif button_id == 54:
        button.config(bg=colors_icon_3state_green[new_state][0], fg=colors_icon_3state_green[new_state][1])
    else:
        button.config(bg=colors_3_state[new_state][0], fg=colors_3_state[new_state][1])

    # Update state in dictionary
    button_states[button_id] = new_state

    # If new state is 2, start blinking
    if new_state == 2:
        blink_button(button, button_id, bg_blink_color)

def toggle_4_button_grid(button, button_id, bg_blink_color,button_press):
    """Toggle button color and text between three states."""
    current_state = button_states[button_id]  # Get current state
    new_state = (current_state + 1) % 4  # Cycle between 0 → 1 → 2
    # Apply new colors
    button.config(bg=colors_4_state[new_state][0], fg=colors_4_state[new_state][1])
    button_press.set(1 if button_press ==0 else 0) # acknowledge button press

    # Update state in dictionary
    button_states[button_id] = new_state

    # If new state is 2, start blinking
    if new_state == 3:
        blink_button(button, button_id, bg_blink_color)
    button_press.set(1 if button_press == 0 else 0)  # acknowledge button press

def add_toggle_4_button_grid(frame, text_stuff, row, col, button_id, fg_blink_color, button_press):
    """Create a toggle button with three color states."""
    button_states[button_id] = 0
    button = tk.Button(frame, text=text_stuff, width=5, height=2, font=("Arial", 16, "bold"),
                       bg=colors_4_state[0][0], fg=colors_4_state[0][1], activebackground="gray",
                       command=lambda: toggle_4_button_grid(button, button_id, fg_blink_color,button_press))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

def add_toggle_3_button_grid(frame, text_stuff, row, col, button_id, fg_blink_color):
    """Create a toggle button with three color states."""
    button = tk.Button(frame, text=text_stuff, width=5, height=2, font=("Arial", 16, "bold"),
                       bg=colors_3_state[0][0], fg=colors_3_state[0][1], activebackground="gray",
                       command=lambda: toggle_3_button_grid(button, button_id, fg_blink_color))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    # Initialize button state
    button_states[button_id] = 0

def blink_button(button, button_id, fg_blink_color):
    """Makes the button blink when in state 2."""
    if button_states[button_id] == 2 or button_states[button_id] == 3:
        # Toggle colors
        current_fg = button.cget("fg")
        new_fg = fg_blink_color if current_fg == "gray" else "gray"
        button.config(fg=new_fg)
        # Schedule next toggle
        button.after(500, lambda: blink_button(button, button_id, fg_blink_color))

def on_switch_print(switch_var, button):
    """Toggle text color of the V2X switch."""
    if switch_var.get() == 1:
        button.config(fg="lightgreen")
    else:
        button.config(fg="gray")

    # Track Longitudinal Switch ON/OFF
    if button == longitudinalSwitch:
        longitudinal_switch_on.set(switch_var.get() == 1)

def speed_change(speed,sign, display):
    speed.set(speed.get() + int(sign))
    display.set(f"{speed.get()} mi/h")
    #print(speed.get())

def main():
    HMI_Window = tk.Tk()
    HMI_Window.title("HMI Example")
    HMI_Window.geometry("1080x720")

    fault_messages_text = "No Messages"
    driving_mode_text = "Driver Mode: Eco"
    CACC_messages_text = "Gap:\n-- m\n Headway:\n-- Sec\nCACC Mileage:\n--mi"


    # Create a PanedWindow to split the window into two resizable sections
    paned_window = tk.PanedWindow(HMI_Window, orient=tk.HORIZONTAL)
    paned_window.pack(fill=tk.BOTH, expand=True)

    # Left side: Scrollable frame for buttons
    left_frame = tk.Frame(paned_window, width=100)  # Adjust the width as needed
    paned_window.add(left_frame, minsize=100)

    canvas = tk.Canvas(left_frame, width=100)
    scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=canvas.yview, width=10)  # Adjust scrollbar width
    scrollable_frame = tk.Frame(canvas, width=100, bg="black")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set, bg="black")

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    acc_on = tk.BooleanVar(value=False)  # ACC ON/OFF
    acc_button_pressed = tk.BooleanVar(value=False)  # ACC button state
    ain_button_pressed = tk.BooleanVar(value=False)  # AIN button state
    lcc_button_pressed = tk.BooleanVar(value=False)  # LCC button state
    longitudinal_switch_on = tk.BooleanVar(value=False)  # Longitudinal Switch ON/OFF

    # Add buttons to the scrollable frame
    add_toggle_button(scrollable_frame, "AIN", 0)
    add_toggle_button(scrollable_frame, "DMS", 1)
    add_toggle_button(scrollable_frame, "DYNO", 2)
    add_toggle_button(scrollable_frame, "LCC", 3)
    add_toggle_button(scrollable_frame, "ACC", 4)

    # Middle: Add other content here
    middle_frame = tk.Frame(paned_window, bg="black")
    middle_frame.pack(expand=True, fill="both")
    paned_window.add(middle_frame)

    text_box = tk.Text(middle_frame,height=3,width=25, font=("Arial", 24,),bg="white", fg="red",
                       highlightbackground="red",highlightcolor="red",highlightthickness=10)
    text_box.pack(side="top", fill="x", padx=10, pady=5)
    text_box.insert("1.0", fault_messages_text)
    text_box.config(state="normal") #makes it read only

    grid_container = tk.Frame(middle_frame, bg="black")
    grid_container.pack(side="top", expand=False, pady=10)  # Center it in the remaining space

    for i in range(5):
        grid_container.columnconfigure(i, weight=1)

    add_toggle_3_button_grid(grid_container, "MIL\nIcon", 0, 0, 50, "darkorange")
    add_toggle_3_button_grid(grid_container, "Vehicle\nAhead\nIcon", 0, 1, 51, "red")
    add_toggle_4_button_grid(grid_container, "ACC\nIcon", 0, 2, 52, "darkorange",acc_button_pressed)
    add_toggle_4_button_grid(grid_container, "AIN\nIcon", 0, 3, 53, "darkorange",ain_button_pressed) # stoplight
    add_toggle_3_button_grid(grid_container, "DMS\nIcon", 0, 4, 54, "darkorange") # dms

    add_toggle_3_button_grid(grid_container, "Battery\nHeat\nIcon", 1, 0, 55, "red")
    add_toggle_3_button_grid(grid_container, "PCM\nHeat\nIcon", 1, 1, 56, "red")
    add_toggle_3_button_grid(grid_container, "V2X\nIcon", 1, 2, 57, "green") #just to see
    add_toggle_3_button_grid(grid_container, "Long\nControl\nIcon", 1, 3, 58, "green") #just to see
    add_toggle_3_button_grid(grid_container, "Lat\nControl\nIcon", 1, 4, 59, "green") #just to see

    add_toggle_3_button_grid(grid_container, "UDP\nIcon", 2, 0, 60, "darkorange")
    add_toggle_3_button_grid(grid_container, "DYNO\nREQ\nIcon", 2, 1, 61, "white")
    add_toggle_3_button_grid(grid_container, "SIM\nOBJ\nIcon", 2, 2, 62, "white")
    add_toggle_4_button_grid(grid_container, "LCC\nIcon", 2, 3, 63, "darkorange",lcc_button_pressed) # stoplight
    #add_toggle_3_button_grid(grid_container, "DMS\nIcon", 2, 4, 64, "darkorange") # dms

    text_box2 = tk.Text(middle_frame, height=1, width=25, font=("Times New Roman", 24,), bg="black", fg="white",
                        highlightbackground="gray", highlightcolor="black", highlightthickness=3)
    text_box2.place(relx=0.5, rely=0.55, anchor="n")
    text_box2.tag_configure("center", justify="center")
    text_box2.insert("1.0", driving_mode_text)
    text_box2.config(state="normal")  # makes it read only

    text_box3 = tk.Text(middle_frame,height=6,width=25, font=("Times New Roman", 24,),bg="black", fg="white",
                        highlightbackground="gray",highlightcolor="white",highlightthickness=10)
    text_box3.place(relx=0.5, rely=0.65, anchor="n")
    text_box3.tag_configure("center", justify="center")
    text_box3.insert("1.0", CACC_messages_text)
    text_box3.config(state="normal") #makes it read only

    # Right: Add other content here
    right_frame = tk.Frame(paned_window, bg="gray")
    paned_window.add(right_frame, stretch="always")

    #HMI_Window.mainloop()

    Non_HMI_Window = tk.Toplevel(HMI_Window, bg="black")
    Non_HMI_Window.title("Switches and Speed")
    Non_HMI_Window.configure(bg="black")
    #window2_label = tk.Label(Non_HMI_Window,bg="black",fg="white", text="this is the window for physical switches and speed")
    #window2_label.pack()


    switch_frame = tk.Frame(Non_HMI_Window, bg="black")
    switch_frame.grid(row=1, column=0, columnspan=3, pady=5)

    v2x_switch_var = tk.BooleanVar()
    lateral_switch_var = tk.BooleanVar()
    longitudinal_switch_var = tk.BooleanVar()
    V2X_Switch_text = "V2X Switch"
    Lateral_Switch_text = "Lateral Switch Switch"
    Longitudinal_Switch_text = "Longitudinal Switch Switch"

    # To change the displayed names of the switches, modify the `text` parameter below
    v2xSwitch = tk.Checkbutton(switch_frame,text=V2X_Switch_text,variable=v2x_switch_var,onvalue=1,offvalue=0,
                               bg="black",fg="gray", relief="raised", command=lambda:on_switch_print(v2x_switch_var, v2xSwitch))
    v2xSwitch.grid(row=0, column=0, padx=5)

    lateralSwitch = tk.Checkbutton(switch_frame,text=Lateral_Switch_text,variable=lateral_switch_var,onvalue=1,offvalue=0,
                                   command=lambda:on_switch_print(lateral_switch_var,lateralSwitch),
                                   bg="black",fg="gray",relief="raised")
    lateralSwitch.grid(row=0, column=1, padx=5)

    longitudinalSwitch = tk.Checkbutton(switch_frame,text=Longitudinal_Switch_text,variable=longitudinal_switch_var,
                                        command=lambda:on_switch_print(longitudinal_switch_var,longitudinalSwitch),
                                        bg="black",fg="gray",relief="raised",onvalue=1,offvalue=0)
    longitudinalSwitch.grid(row=0, column=2, padx=5)


    speed_frame = tk.Frame(Non_HMI_Window, bg="black")
    speed_frame.grid(row=2, column=0, columnspan=3, pady=10)

    speed_val = tk.IntVar(value=0)
    speed_display = tk.StringVar(value="0 mi/h")  # StringVar to display formatted speed

    decrement_speed = tk.Button(speed_frame, text="-",width=2,command=lambda:speed_change(speed_val,-1,speed_display),
                                bg="black", fg="gray", relief="raised")
    decrement_speed.grid(row=0, column=0, padx=5, pady=5)

    speed_label = tk.Label(speed_frame, textvariable=speed_display, bg="black", fg="white",
                           font=("Arial", 16))
    speed_label.grid(row=0, column=1, padx=5, pady=5)

    increment_speed = tk.Button(speed_frame, text="+",width=2, command=lambda:speed_change(speed_val,1,speed_display),
                                bg="black", fg="gray",relief="raised")
    increment_speed.grid(row=0, column=2, padx=5, pady=5)

    set_and_res_frame = tk.Frame(Non_HMI_Window, bg="black")
    set_and_res_frame.grid(row=4, column=0, columnspan=3, pady=10)

    set_speed_button = tk.Button(set_and_res_frame, text="SET-", borderwidth=10, highlightthickness=0, width=6,
                       height=1, font=("Arial", 12), bg="black", fg="white", activebackground="gray",
                       activeforeground="black")
    set_speed_button.grid(row=0, column=0, padx=5, pady=5)
    reset_speed_button = tk.Button(set_and_res_frame, text="RES+", borderwidth=10, highlightthickness=0, width=6,
                       height=1, font=("Arial", 12), bg="black", fg="white", activebackground="gray",
                       activeforeground="black")
    reset_speed_button.grid(row=0, column=2, padx=5, pady=5)

    # Centering the speed frame in the window
    Non_HMI_Window.grid_columnconfigure(0, weight=1)
    Non_HMI_Window.grid_columnconfigure(1, weight=1)
    Non_HMI_Window.grid_columnconfigure(2, weight=1)
    Non_HMI_Window.grid_columnconfigure(3, weight=1)
    Non_HMI_Window.grid_columnconfigure(4, weight=1)

    #Non_HMI_Window.mainloop()
    HMI_Window.mainloop()

if __name__ == "__main__":
    main()
