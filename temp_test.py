import pixel_util
import controller
import model

test_size = (3, 3)
test_corners = [(1,1), (3,3), (3,1), (1,3)]

m = model.ImgModel(test_size, test_corners)
c = controller.ImgController(m)
