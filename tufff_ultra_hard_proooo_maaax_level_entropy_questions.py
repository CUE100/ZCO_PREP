def tufff_ultra_hard_proooo_maaax_level_entropy_deluxeee_question_GTA6_67_67_faaaah(contests,v,w):
    
    times = []
    for s,e in contests:
        best_v = v[0]
        best_w = w[0]
        for x in v:
            if x <= s:
                if x >= best_v:
                    best_v = x

        for y in w:
            if y >= e:
                if y <= best_w:
                    best_w = y
        time = y-x+1
        times.append(time)
    minimum = min(times)
    return minimum
    

        

    
