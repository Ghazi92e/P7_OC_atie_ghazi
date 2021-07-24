from parsing.stop_words import STOP_WORDS


class Parse:
    @staticmethod
    def filterdata(data_user):
        """Used to parse the address send by the user"""
        filter_data = []
        for data in data_user.split():
            if data not in STOP_WORDS:
                filter_data.append(data)
        return filter_data
