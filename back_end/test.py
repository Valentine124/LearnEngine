
import models
from models.resources import Resources



print(models.storage.all_resources())

resource = Resources()
resource.title = 'Data Structure'
resource.description = 'descr'
resource.origin = 'origin'
resource.type = 'type'
resource.url = 'url'

models.storage.new(resource)

print(models.storage.all_resources())

resource = Resources()
resource.title = 'Data Structure'
resource.description = 'descr'
resource.origin = 'origin'
resource.type = 'type'
resource.url = 'url'

models.storage.new(resource)
print(models.storage.all_resources())

models.storage.close()
