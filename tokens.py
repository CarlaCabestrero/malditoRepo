class Tokens:

	def __init__(self):
		facebook_WeatherBot_token = "EAAEGgHE2HqsBACcxBhVaejIKhe9ovXabfs6842IuAgz5w5lgjZAdOJNL2zB5lOySFDszCZAHOQfULiyvjXrg8S8MeOWZAJuMWpYz1QcRKmZA6L5arp7i7MysEdKzu8vWQsCLQs8UYsN62jtZCTYs8tavZBjdRB313jFFVGAlliQQZDZD"
		telegram_PepeJuanBot_token = "442017555:AAECxTQYrjtAwKn6hMvYIHbZif_XIFupkzA"
		telegram_PepeJuanProBot_token = "506490097:AAENS0l9hM646svObHbRgkEryl3_fR00PPE"

		self.names = [
			"WeatherBot_facebook",
			"PepeJuanBot_telegram",
			"PepeJuanProBot_telegram"
		]

		self.tokens = [
			facebook_WeatherBot_token,
			telegram_PepeJuanBot_token,
			telegram_PepeJuanProBot_token
		]
		self.dictionary = self.getDic()


	def getDic(self,):
		return dict([(self.names[i],self.tokens[i]) for i in range(len(self.names))])





	def getTokens(self, botname):

		return self.dictionary[botname]


def getBotToken(botname):
	token = Tokens()
	return(token.getTokens(botname))




