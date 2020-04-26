from marshmallow import fields, Schema


class ShowLookupSchema(Schema):
	added = fields.Str()
	airTime = fields.Str()
	certification = fields.Raw()
	cleanTitle = fields.Str()
	firstAired = fields.DateTime()
	genres = fields.List(fields.Str())
	id = fields.Int()
	images = fields.Raw()
	imdbId = fields.Str()
	languageProfileId = fields.Int()
	lastInfoSync = fields.Str()
	monitored = fields.Bool()
	network = fields.Str()
	overview = fields.Str()
	path = fields.Str()
	profileId = fields.Int()
	qualityProfileId = fields.Int()
	ratings = fields.Raw()
	remotePoster = fields.Url()
	runtime = fields.Int()
	seasonCount = fields.Int()
	seasonFolder = fields.Bool()
	seasons = fields.Raw()
	seriesType = fields.Str()
	sortTitle = fields.Str()
	status = fields.Str()
	tags = fields.Raw()
	title = fields.Str()
	titleSlug = fields.Str()
	tvdbId = fields.Int()
	tvMazeId = fields.Int()
	tvRageId = fields.Int()
	useSceneNumbering = fields.Bool()
	year = fields.Int()