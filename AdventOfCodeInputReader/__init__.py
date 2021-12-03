import requests
import logging
import traceback

logger = logging.getLogger('AdventOfCodeInputReader')
logger.setLevel(logging.ERROR)

class AdventOfCodeInputReader:
    """
    Class for getting Advent Of Code Input
    """
    def __init__(self, session_id,year=None,day=None):
        self.session_id = session_id
        self.year = year
        self.day = day

    def get_input(self,day=None,year=None):
        """
        If value for day and year parameters are specified, they will override the year and day declared at initialization for this method.
        """
        if not day:
            if self.day:
                day = self.day
            else:
                raise Exception("No Day specified.")
        if not year:
            if self.year:
                year = self.year
            else:
                raise Exception("No Year specified.")
        try:
            response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', headers={"Cookie":"session="+self.session_id})
            if response.status_code == 200:
                return response.content.decode("utf-8").split("\n")[:-1]
            else:
                raise Exception("Incorrect Day, Year, or Session ID. Please ensure that Day, Year, and Session ID are correct.")
        except Exception as e:
            logger.error(f"{str(e)}\n\n{''.join(traceback.format_tb(e.__traceback__))}")
            raise e
        
    def get_input_by_day(self,day):
        """
        Method requires Year to be set up at initialisation.
        The day argument provided will override the day provided at inialisation for this method only.
        """
        if not self.year:
            raise Exception("No Year specified. Please specify Year at initialization.")
        try:
            response = requests.get(f'https://adventofcode.com/{self.year}/day/{day}/input', headers={"Cookie":"session="+self.session_id})
            return response.content.decode("utf-8").split("\n")[:-1]
        except Exception as e:
            logger.error(f"{str(e)}\n\n{''.join(traceback.format_tb(e.__traceback__))}")
            raise e

    def get_input_by_day_and_year(self,day,year):
        """
        The day and year arguments provided will override the day and year provided at inialisation (if any) for this method only.
        """
        if not self.year:
            raise Exception("No Year specified. Please specify Year at initialization.")
        try:
            response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', headers={"Cookie":"session="+self.session_id})
            return response.content.decode("utf-8").split("\n")[:-1]
        except Exception as e:
            logger.error(f"{str(e)}\n\n{''.join(traceback.format_tb(e.__traceback__))}")
            raise e