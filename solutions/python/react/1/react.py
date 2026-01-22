class InputCell:
    def __init__(self, initial_value):
        self.callbacks = set()
        self.value = initial_value

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        for func in self.callbacks:
            func(value)

    def add_callback(self, func):
        self.callbacks.add(func)

    def remove_callback(self, callback):
        if len(self.callbacks) > 1:
            self.callbacks.remove(callback)

class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.callbacks = set()
        self.inputs = inputs
        self.compute_function = compute_function
        self.updated = [False] * len(inputs) # flags for updating ComputeCell only when all dependencies updated
        
        input_values = [k.value for k in self.inputs]
        self.value = self.compute_function(input_values)

        for i, input in enumerate(inputs):
            input.add_callback(lambda x, i=i: self.recompute(x, i)) # Pass input index as an argument to recompute for flagging

    def recompute(self, changed_input, index):
        # Set the flag for the changed input to True
        self.updated[index] = True

        if all(self.updated):
            input_values = [k.value for k in self.inputs]
            new_value = self.compute_function(input_values)
            if new_value != self.value:
                self.value = new_value
                for func in self.callbacks:
                    func(new_value)

            # Reset all flags to False after updating ComputeCell's value
            self.updated = [False] * len(self.inputs)
        
    def add_callback(self, callback):
        self.callbacks.add(callback)
    
    def remove_callback(self, callback):
        if len(self.callbacks) > 1:
            self.callbacks.remove(callback)