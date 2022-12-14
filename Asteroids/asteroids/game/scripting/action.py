class Action:
    """A thing that is done.
    
    The responsibility of action is to do something that is integral or important in the game. 
    It has one method, execute(), which is overridden by derived classes.
    """

    def execute(self, cast, script):
        """Executes something that is important in the game. This method is overriden by 
        derived classes.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        pass