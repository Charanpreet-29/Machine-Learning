$true = shift;
open(IN,$true);
while(<IN>){
	chomp $_;
	@s=split(/\s+/,$_);
	$truelabels{$s[1]}=$s[0];
} close IN;

$predict=shift;
open(IN,$predict);
while(<IN>) {
	chomp $_;
	@s=split(/\s+/,$_);
	if(defined($truelabels{$s[1]})){
	 $precitedlabels{$s[1]}=$s[0];
	}
} close IN;

#for(my $i=0; $i<scalar(@cl); $i++) { print $cl[$i]."\n";}
#foreach my $x (keys %testclass) { print "$x $testclass{$x}\n";}
#foreach my $x (keys %trueclass) { print "$x $testclass{$x}\n";}
#foreach my $x (keys %testclass) { print "$x $testclass{$x}\n";}

$a = $b = $c = $d = 0;
$error =0;
foreach my $x (keys %precitedlabels) {
	if($truelabels{$x} == 0 && $precitedlabels{$x} == 0) { $a++; }
	if($truelabels{$x} == 0 && $precitedlabels{$x} == 1) { $b++; }
	if($truelabels{$x} == 1 && $precitedlabels{$x} == 0) { $c++; }
	if($truelabels{$x} == 1 && $precitedlabels{$x} == 1) { $d++; }
	}

$BER = 0.5 * ( $b /($a+$b) + $c /($c+$d));
print "$BER";


