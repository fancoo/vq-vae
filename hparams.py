# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com.
https://www.github.com/kyubyong/vq-vae
'''
class Hyperparams:
    '''Hyper parameters'''

    # data
    data = "/data/public/rw/datasets/VCTK-Corpus/wav48/*/*"
    test_data = '''p227_363|2|we are encouraged by the news.
                   p231_430|6|it was a breathtaking moment.'''
    speakers = ("p225", "p226", "p227", "p228", "p229", "p230", "p231", "p232", "p233", "p234", "p236", "p237", "p238", "p239", "p240", "p241", "p243", "p244", "p245", "p246", "p247", "p248", "p249", "p250", "p251", "p252", "p253", "p254", "p255", "p256", "p257", "p258", "p259", "p260", "p261", "p262", "p263", "p264", "p265", "p266", "p267", "p268", "p269", "p270", "p271", "p272", "p273", "p274", "p275", "p276", "p277", "p278", "p279", "p280", "p281", "p282", "p283", "p284", "p285", "p286", "p287", "p288", "p292", "p293", "p294", "p295", "p297", "p298", "p299", "p300", "p301", "p302", "p303", "p304", "p305", "p306", "p307", "p308", "p310", "p311", "p312", "p313", "p314", "p315", "p316", "p317", "p318", "p323", "p326", "p329", "p330", "p333", "p334", "p335", "p336", "p339", "p340", "p341", "p343", "p345", "p347", "p351", "p360", "p361", "p362", "p363", "p364", "p374", "p376")

    # signal processing
    sr = 16000  # Sampling rate.
    Q = 256 # quantization_channels
    duration = 2 # second
    T = int(duration * sr) # Fixed time dimensionality.

    # Model
    ## encoder
    encoder_layers = 6
    winsize = 4
    stride = 2

    ## vq
    D = 512 # Dimensionality of embedding
    K = 128 # Number of categories

    ## decoder (wavenet)
    num_blocks = 2 #10
    dilations = (1, 2, 4, 8, 16, 32)
    size = 3 # filter width
    num_units = 256

    # training scheme
    lr = 0.0001 # learning rate.
    logdir = "logdir/08"
    sampledir = 'samples'
    batch_size = 4 # B
    beta = 0.25

