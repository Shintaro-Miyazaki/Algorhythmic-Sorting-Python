(
SynthDef("grain", { |out, amp=0.1, freq=440, sustain=0.01, pan|
	var snd = FSinOsc.ar(freq);
	var amp2 = amp * AmpComp.ir(freq.max(50)) * 0.5;
	var env = EnvGen.ar(Env.sine(sustain, amp2), doneAction: 2);
	OffsetOut.ar(out, Pan2.ar(snd * env, pan)); }, \ir ! 5).add;
)

s.sendMsg("s_new", \grain, -1, 0, 1, \freq, 500, \sustain, 0.1, \pan, -1.0); 