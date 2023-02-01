


def resnet_34(image):
    transform = transforms.Compose([ 
        transforms.ToTensor(),
        transforms.Normalize(mean=ApiConfig.mean, std=ApiConfig.std), ])
    image = transform(image).unsqueeze(0)

    y = ApiConfig.model(image)
    m = torch.argmax(y.data, dim=1).numpy()[0]
       
    if m == 1: resp = 'clean'
    else: resp = 'dirty'
    print(resp)
    return resp


