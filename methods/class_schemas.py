#!/usr/bin/env python3
from marshmallow import fields, Schema


# noinspection PyUnusedName,PyUnusedName
class ImageSchema(Schema):
	coverType = fields.Str()
	url = fields.Url()


# noinspection PyUnusedName,PyUnusedName
class SeasonsListSchema(Schema):
	seasonNumber = fields.Int()
	monitored = fields.Bool()


# noinspection PyUnusedName,PyUnusedName
class RatingsSchema(Schema):
	votes = fields.Int()
	value = fields.Int()


# noinspection PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,
# PyUnusedName,PyUnusedName
# noinspection PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,
# PyUnusedName,PyUnusedName
# noinspection PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName,
# PyUnusedName,PyUnusedName
# noinspection PyUnusedName,PyUnusedName,PyUnusedName,PyUnusedName
class ShowLookupSchema(Schema):
	added = fields.Str()
	airTime = fields.Str()
	certification = fields.Raw()
	cleanTitle = fields.Str()
	firstAired = fields.DateTime()
	genres = fields.List(fields.Str())
	id = fields.Int()
	images = fields.List(fields.Nested(ImageSchema()))
	imdbId = fields.Str()
	languageProfileId = fields.Int()
	lastInfoSync = fields.Str()
	monitored = fields.Bool()
	network = fields.Str()
	overview = fields.Str()
	path = fields.Str()
	profileId = fields.Int()
	qualityProfileId = fields.Int()
	ratings = fields.Nested(RatingsSchema())
	remotePoster = fields.Url()
	runtime = fields.Int()
	seasonCount = fields.Int()
	seasonFolder = fields.Bool()
	seasons = fields.Raw()  # fields.List(fields.Nested(SeasonsListSchema()))
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
