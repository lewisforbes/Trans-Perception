class Tweet:
    def __init__(self, id, date, text, user, like_count, retweet_count):
        self.id = id
        self.date = date
        self.text = text.replace("\n", "[[NEWLINE]]")
        self.like_count = like_count
        # self.is_quote = is_quote
        # self.is_retweet = is_retweet
        self.retweet_count = retweet_count
        self.user = user
        self.about = self.about_who(self.text.lower().replace("\"", "").replace("\'", ""))
    
    def about_who(self, text):
        output = ""
        prefixes = ["trans", "trans ", "transgender "]
        current = "M"
        for gender in [["man", "men"], ["woman", "women"]]:
            for prefix in prefixes:
                for suffix in gender:
                    if (prefix + suffix) in text:
                        output += current
            current = "F"
        if output=="":
            raise Exception("no keyword found in text (ID={}): {}".format(self.id, text))
        if "M" in output and "F" in output:
            return "Both"
        if "M" in output:
            return "M"
        if "F" in output:
            return "F"
