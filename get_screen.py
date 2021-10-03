import tkinter as tk


def get_curr_screen_geometry():
    """
    Workaround to get the size of the current screen in a multi-screen setup.

    Returns:
        geometry (str): The standard Tk geometry string.
            [width]x[height]+[left]+[top]
    """
    root = tk.Tk()

    root.wait_visibility(root)
    root.wm_attributes('-alpha',0.8)

    # Create text widget and specify size.
    T = tk.Text(root, height = 5, width = 52)
    
    # Create label
    l = tk.Label(root, text = "Olof Cum")
    l.config(font =("Helvetica Standard Nemiga", 200))

    l.pack()

    root.update_idletasks()
    root.attributes('-fullscreen', True)
    root.state('iconic')
    geometry = root.winfo_geometry()
    root.destroy()
    return geometry

print(get_curr_screen_geometry())