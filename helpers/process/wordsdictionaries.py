designDict = [
    'did not', 
    'last', 
    'uncomfortable', 
    'durable', 
    'comfort', 
    'tear', 'tips', 
    'eartips', 'sponge', 'wearout', 'break', 'broke', 'broken','cable', 'plastic', 
    'fit', 'cheap', "don't stay", 'sturdy', 'sweat', 'gym', 'fall off', 'connector', 
    'controls', 'slip', 'tight', 'loose',' silicone', 'build'
]
valueDict = [
    'price', 'expensive', 'cheaper', 'cheap', 'money', 'cost'
]
batteryDict = [
    'last', 'day', 'life', 'battery life', 'charge', 'short', 'batteries'
    ]
audioDict = [
    'bass', 'sharp' ,'shrill', 'noise', 'noise cancellation', 'sound', 'sound quality',
    'left channel', 'right channel', 'bleed', 'crisp', 'response', 'clear', 'sound',
    'surrounding', 'static', 'eq', 'equilizer', 'equiliser', 'static', 'low end', 'volume',
    'loud', 'left ear', 'right ear', 'muffled', 'ear pain', 'sounds like', 'in and out'
]
callDict = [
    'hear', 'person', 'speak', 'words', 'break', 'not clear', 'disconnect', 'call', 'call drop',
    'call', 'drop', "can't hear", 'mic', 'muffled', 'hear properly'
]
connectivityDict  = [
    'disconnect', 'drop', 'connect', 'connection', 'bluetoothh', 'pair', 'phone', 'android', 'iphone'
    'wireless', 're-pair', 'spotty', 'others', 'complain', 'link', 'range', 'call drop'
]
commonDict        = [
    'horrible', 'sorry', "don't buy", 'minimal', 'issue', 'needs', 'should', 'could', 'can', 'trouble'
    'down hill', 'poor', 'dissapoint', 'dissapointed', 'dissapointing', 'defective', 'return', 'refund',
    'irrirate', 'irritated', 'irritation', 'sucked', 'suck', 'shit', 'bullshit'
]

def getCatDicts():

    return {
        'design':designDict, 
        'value':valueDict, 
        'battery':batteryDict, 
        'audio':audioDict,
        'call': callDict,
        'connectivity':connectivityDict, 
        #'commonDict':commonDict
    }

#print (getCatDicts())


