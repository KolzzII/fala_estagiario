from application.model.entity.Post import Post
from application.model.dao import postDAO

postDAO.insert_post(Post("Junior", "Me da 10 ai professor s2"))
postDAO.insert_post(Post("Tassio", "Excelente site!!"))