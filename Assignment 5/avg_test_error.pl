$mean = 0;
$data = shift;
$dir=$data;


print "Nearest Means\n";
for(my $i=0; $i<10; $i++){
  system("python3 nearestMeans.py $dir/$data.data $dir/$data.trainlabels.$i > nm_out.$data");
    $err[$i] = `perl error.pl $dir/$data.labels nm_out.$data`;
      chomp $err[$i];
      print "Error = $err[$i]\n";      
      $mean += $err[$i];
     }
	  $mean /= 10;
          $sd = 0.001;
	  for(my $i=0; $i<10; $i++){
            $sd += ($err[$i]-$mean)**2;
            }
          $sd /= 10;
          $sd = sqrt($sd);
	  $mean=$mean*100;
          print "Mean error = $mean ($sd)\n";


$mean = 0;
print "Naive Bayes \n";
for(my $i=0; $i<10; $i++){
    system("python3 naiveBayes.py $dir/$data.data $dir/$data.trainlabels.$i > nb_out.$data");
        $err[$i] = `perl error.pl $dir/$data.labels nb_out.$data`;
         chomp $err[$i];
         print "Error = $err[$i]\n";
         $mean += $err[$i];
      }
	 $mean /= 10;
         $sd = 0.001;
         for(my $i=0; $i<10; $i++){
             $sd += ($err[$i]-$mean)**2;
         }
         $sd /= 10;
         $sd = sqrt($sd);
	 $mean=$mean*100;
         print "Mean error = $mean ($sd)\n";

$mean = 0;
print "Least squares - Adaptive eta \n";
for(my $i=1; $i<2; $i++){
  system("python3 least_squares_adaptive_eta.py $dir/$data.data $dir/$data.trainlabels.$i $eta $stop > p_out.$data");
    $err[$i] = `perl error.pl $dir/$data.labels p_out.$data`;
      print "Error = $err[$i]\n";
      chomp $err[$i];
      $mean += $err[$i];
     }
          $mean /= 1;
          $sd = 0;
          for(my $i=1; $i<2; $i++){
            $sd += ($err[$i]-$mean)**2;
            }
            $sd /= 1;
            $sd = sqrt($sd);
	    $mean=$mean*100;
            print "Mean error = $mean ($sd)\n";

$mean = 0;
print "Hinge Loss - Adaptive eta \n";
for(my $i=1; $i<2; $i++){
     system("python3 hinge_adaptive_eta.py $dir/$data.data $dir/$data.trainlabels.$i $eta $stop > p_out");
     $err[$i] = `perl error.pl $dir/$data.labels p_out`;
     print "Error = $err[$i]\n";
     chomp $err[$i];
     $mean += $err[$i];
   }
	$mean /= 1;
        $sd = 0;
        for(my $i=1; $i<2; $i++){
            $sd += ($err[$i]-$mean)**2;
           }
            $sd /= 1;
            $sd = sqrt($sd);
	    $mean=$mean*100;
            print "Mean error = $mean ($sd)\n";

#                        q^
#                        $mean = 0;
#                        for(my $i=0; $i<10; $i++){
#                          ##Create the training data and labels for SVM

                            ##Obtain the cross-validated value of C
#                              $C = `perl cv-svm.pl data_cv labels_cv`;

                                ##Predict with that value of C
#                                  system("perl run_svm_light.pl $data.data $data.trainlabels.$i $C");
#                                    $err[$i] = `perl error.pl $data.labels svmpredictions`;
#                                      chomp $err[$i];
#                                        $mean += $err[$i];
#                                        }
#                                        $mean /= 10;
#                                        $sd = 0;
#                                        for(my $i=0; $i<10; $i++){
#                                          $sd += ($err[$i]-$mean)**2;
#                                          }
#                                          $sd /= 10;
#                                          $sd = sqrt($sd);
#                                          print "SVM error = $mean ($sd)\n";
#                                        ^if 0;
