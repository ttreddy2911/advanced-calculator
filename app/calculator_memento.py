class Memento:
    """
    Stores a snapshot of calculator state.
    """

    def __init__(self, state):
        self._state = state.copy()

    def get_state(self):
        return self._state.copy()


class Caretaker:
    """
    Manages undo and redo stacks.
    """

    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, state):
        self._undo_stack.append(Memento(state))
        self._redo_stack.clear()  # Clear redo when new action performed

    def undo(self, current_state):
        if not self._undo_stack:
            return current_state

        memento = self._undo_stack.pop()
        self._redo_stack.append(Memento(current_state))
        return memento.get_state()

    def redo(self, current_state):
        if not self._redo_stack:
            return current_state

        memento = self._redo_stack.pop()
        self._undo_stack.append(Memento(current_state))
        return memento.get_state()