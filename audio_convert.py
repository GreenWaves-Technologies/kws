


      ncoeff=40
      n_win = int(100-2)
      tab2D = mfcc(signal,samplerate=model_settings['sample_rate'],winlen=model_settings['window_size_s'],winstep=model_settings['window_stride_s'],nfilt=ncoeff,numcep=model_settings['dct_coefficient_count'], winfunc = numpy.hamming)
      if save_features :
        # dumpp file in a 40*98 pgm image with  16bits pixels
        s_16b = np.array(ncoeff*n_win)
        #shift left by 7 bits
        s_16b = (tab2D*128).astype(int)
        #np.savetxt("./SAVE_WAVES/feature.txt_"+ str(i),s_16b, fmt='%d', delimiter=",", newline="\n")
        #with open("./data/feature.txt_" + str(i) + ".pgm", 'wb') as f:
        #  hdr =  'P5' + '\n' + str(ncoeff) + '  ' + str(n_win) + '  ' + str(65535) + '\n'
        #  f.write(hdr.encode())
        #  s_16b.tofile(f)
      #number of overlapping windows
      data[i - offset, :] = np.reshape(tab2D,model_settings['dct_coefficient_count']*(n_win))
      label_index = self.word_to_index[sample['label']]
      labels[i - offset, label_index] = 1
