import tkinter as tk

class NegativeButton(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self['bg'] = 'coral'
        self['activebackground'] = 'dark slate gray'
        self['cursor'] = 'hand2'
        self['highlightbackground'] = 'blanched almond'
        self['activeforeground'] = 'blanched almond'
        
        

class PositiveButton(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self['bg'] = 'blanched almond'
        self['activebackground'] = 'dark slate gray'
        self['cursor'] = 'hand2'
        self['highlightbackground'] = 'blanched almond'
        self['activeforeground'] = 'blanched almond'
        
        

