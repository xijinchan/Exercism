class InputCell:
    
    def __init__(self, initial_value):
        self.update_flag_callbacks = set() # notify all following cells first of pending update to avoid unnecessary callbacks
        self.callbacks = set() # callbacks for passing new values
        self.value = initial_value

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        try: 
            for func in self.update_flag_callbacks: # notify all linked cells first
                func(value)
        except:
            pass  
        try:
            for func in self.callbacks:
                func(value)
        except:
            pass

    def add_callback(self, func):
        self.callbacks.add(func)

    def remove_callback(self, callback):
        if len(self.callbacks) > 1:
            self.callbacks.remove(callback)

    def add_update_flag_callbacks(self, func):
        self.update_flag_callbacks.add(func)

class ComputeCell:
    number = 1
    def __init__(self, inputs, compute_function):
        self.update_flag_callbacks = set()
        self.callbacks = set()
        self.inputs = inputs
        self.compute_function = compute_function
        self.update_pending_flags = [False] * len(inputs) # flag which inputs are pending an update
        self.updated = [False] * len(inputs) # update only when all 'self.update_pending_flags' flagged inputs have updated
        
        input_values = [k.value for k in self.inputs]
        self.value = self.compute_function(input_values)

        for i, input in enumerate(inputs):
            input.add_update_flag_callbacks(lambda x, i=i: self.update_pending_flags_func(x, i)) # do flags first

        for i, input in enumerate(inputs):
            input.add_callback(lambda x, i=i: self.recompute(x, i)) # Pass input index as an argument to recompute for flagging

    def recompute(self, changed_input, index):
        self.updated[index] = True # Set the flag for the changed input to True

        if all([True if self.updated[m] else False for m in [i for i,k in enumerate(self.update_pending_flags) if k == True]]): # only when all inputs with update_pending_flags have been updated 
            input_values = [k.value for k in self.inputs]
            new_value = self.compute_function(input_values)
            if new_value != self.value:
                self.value = new_value
                for func in self.callbacks:
                    func(new_value)

            # Reset all flags to False after updating ComputeCell's value
            self.updated = [False] * len(self.inputs)

    def update_pending_flags_func(self, changed_input, index): # changed_input = changed_input.value
        self.update_pending_flags[index] = True
        try:
            for func in self.update_flag_callbacks:
                func(changed_input)
        except:
            pass
        
    def add_callback(self, callback):
        self.callbacks.add(callback)
    
    def remove_callback(self, callback):
        if len(self.callbacks) > 1:
            self.callbacks.remove(callback)

    def add_update_flag_callbacks(self, func):
        self.update_flag_callbacks.add(func)
        
        