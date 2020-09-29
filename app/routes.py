from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse

import gensim
import collections
from app import app, db
from app.forms import TokenListForm, SimilarityForm, LoginForm, RegistrationForm
from app.models import User, Post

model = gensim.models.Word2Vec.load(r"D:\Workplace\code\python_flask_sample\tweet_ps.model")
w2c = dict()
for item in model.wv.vocab:
    w2c[item]=model.wv.vocab[item].count
sorted_x = sorted(w2c.items(), key=lambda kv: kv[1], reverse=True)
#w2cSorted = dict(sorted(w2c.items(), key=lambda x: x[1],reverse=True))
w2cSorted = collections.OrderedDict(sorted_x)

anew = ['abang','aborsi','abu','acar','acara','adat','aerobik','agar-agar','agresif','air','air terjun','akal','aksi','akta','aktivis','alam','alami','alasan','alat','alergi','alis','aljabar','alkohol','alun-alun','aman','ambisi','ambisius','amis','amok','amoral','anak','anak-anak','ancaman','aneh','anggun','anggur','angin','anjing','anjing kecil','antarnegara','api','arah','arang','arif','aritmetika','arogan','asam','asap','asing','asmara','astronot','asyik','atletik','atmosfer','awan','ayah','babi','badai','badan','bagian','bagus','bahagia','bahasa','bahaya','baik','bajing','bajingan','bak','bakat','balai kota','banci','bandara','bangga','bangkai','bangkrut','bangku','bangsa','bangsat','bangun','banjir','bank','bantal','bantuan','bar','barang','barbel','batang','batasan','batu','bau','bayangan','bayi','beban','bebas','becek','bedah','bedeng','bedil','bekas','beku','belajar','belati','belatung','benak','bencana','benci','bendahara','bendera','bendungan','bentrokan','beracun','berahi','berang','berani','berbagi','berbaring','berbohong','berbudaya','bercela','berdebar','berdenyut','berdetak','berdosa','bergairah','bergembira','bergulir','berguna','berharap','beri-beri','berisik','berita','berjuang','berkarat','berkelahi','berkuasa','berlian','bermain-main','bermartabat','bermasalah','bermusuhan','berotot','bersahabat','bersalah','bersenyawa','berseri','bersiul','bersorak','bersyukur','bertanya-tanya','bertenaga','bertengkar','berteriak','berterimakasih','bertunangan','beruang','beruntung','besar hati','besi','betis','biadab','biarawati','biasa','bibi','bibir','bijaksana','bimbang','binatang buas','bingung','bintang','biola','biri-biri','biru','bocah','bodoh','bohlam','bom','boneka','bosan','botol','brutal','buah','budak','bugil','bui','buket','buku','bulan','bulu','bulu tangkis','bumbu','bumi','bunga','bunuh','bunuh diri','burung','burung hantu','bis','busa','busuk','buta','cabul','cacar','cacat','cadangan','cakar','cakram','campak','candi','cantik','capek','cara','catur','cela','cemar','cemas','cemburu','cendawan','cendekiawan','cendol','cengkih','cepat','cerah','ceria','cetakan','cibiran','cinta','ciuman','cokelat','cuek','curiga','cuti','dada','dadar','dagu','dahak','dahsyat','daki','damai','danau','dapur','darah','dataran','daun','daya tarik','debit','definisi','dekret','demam','demen','demokrasi','dendam','dengki','deposito','depresi','desa','desain','detail','dewasa','dibakar','dihormati','dikagumi','dikasihi','dingin','dipan','dipermalukan','direktur','diri','diskotek','dokter','dokter gigi','dolar','domisili','dongkol','dosa','dosen','dubur','duka','dukacita','dunia','duri','dusun','edan','egois','ejekan','eksekusi','ekstasi','ekuivalen','elang','elevator','emas','emosi','empuk','energik','enggan','erotis','evaluasi','fajar','fantasi','fase','film','firdaus','frase','frekuensi','frustasi','gabus','gadis','gagah','gaib','gairah','galau','ganas','gang','gangguan','garam','garmen','garpu','garuda','gaun','gedung','gelap','geli','gelisah','gemas','gembira','gembong','gempa','gemuk','gengsi','gentar','gerai','geram','gereja','gerobak','getar hati','getir','gigi','gila','girang','giring-giring','gletser','gol','golok','gosip','granat','gratis','gregetan','gua','gudang','gugatan','gugup','gula','gumpalan','gundah','gunting','gunung','gunung api','gurih','guru','gusar','guyon','hadiah','hadir','haji','hak','hakikat','halus','hama','hancur','hansip','harapan','hari','harimau','harta karun','haru','hasrat','hati','hebat','heran','heroin','hidran','hidung','hidup','hijau','hilang','hina','hinaan','histeris','hitam','hiu','hiu','hormat','hostel','hotel','hubungan','hujan','hukuman','humor','huru-hara','iba','iblis','ibu','ide','identitas','idiot','idola','ijazah','ikan','ikhlas','ikut-ikutan','imbalan','impoten','industri','infeksi','inferior','infrastruktur','ingatan','ingin','ingin tahu','insentif','intelijen','internet','intim','intimidasi','iri','istana','istirahat','istri','jagoan','jahat','jalan','jalan besar','jalan raya','jam','jamur','janggal','jantung','jari','jarum','jatuh','jauh','jawaban','jaya','jelek','jelita','jendela','jender','jengkel','jenuh','jerami','jerat','jeritan','jijik','jimat','jinak','jiwa','joget','juara','jujur','jurang','jurnal','juru','jurusan','jus','jutawan','kabar','kabinet','kaca','kacamata','kacau','kagum','kaidah','kain','kaki','kaku','kalah','kalajengking','kalap','kalut','kamar','kamar mayat','kambing hitam','kampus','kanal','kangen','kanker','kantong','kantor','kapal','kapal pesiar','kapur','karantina','karier','kartu as','kas','kasar','kasih','kasih sayang','kasihan','kasino','kasir','kasmaran','katak','kaus kaki','kaya','keadilan','keajaiban','kebahagiaan','kebaikan','kebajikan','kebanggaan','kebanjiran','kebebasan','kebenaran','kebencian','keberangan','kebetulan','kebiadaban','kebiasaan','kebodohan','kebosanan','kebun','kecamatan','kecanduan','kecantikan','kecelakaan','kecemasan','kecemburuan','kecerdasan','kecewa','kecil','kecil hati','kecoak','kedengkian','kegagalan','kegandrungan','kegembiraan','kehangatan','keharuan','keharuman','keheranan','kehidupan','kehormatan','keinginan','kejahatan','kejam','kejayaan','kekacauan','kekasih','kekayaan','kekeliruan','kekhawatiran','keki','kekuasaan','kekuatan','kelaparan','kelelawar','kelimpahan','kelincahan','kelinci','keluarga','kelumpuhan','kemajuan','kemarahan','kematian','kembang api','kemenangan','kemerdekaan','kemesraan','kemewahan','kemiskinan','kemuliaan','kenakalan','kenangan','kencing','kendala','kendaraan','kendi','kengerian','kenikmatan','kentut','kenyamanan','kepala pelayan','keperawatan','kepingin','kepuasan','keranjang','keras','kereta','keriangan','kertas','kerusakan','kerusuhan','kesakitan','kesal','kesedihan','kesehatan','kesejahteraan','kesempatan','kesempurnaan','kesenangan','kesendirian','kesengsaraan','kesepakatan','kesepian','keserakahan','kesombongan','kesopanan','kesulitan','kesuraman','kesusahan','ketakjuban','ketakutan','ketel','ketenaran','ketiak','keunggulan','keuntungan','kewalahan','khawatir','khidmat','kikuk','kincir angin','koin','kolam','kolom','kolumnis','komedi','komentator','komet','komisaris','kompor','komputer','komunis','konferensi','konsentrasi','konsolidasi','konteks','kontrarevolusioner','konveksi','konyol','kopi','koran','korban','koridor','korup','kota','kotor','kotoran','kredit','krisis','kuadrat','kualitas','kuat','kuburan','kucing','kuda','kue','kue mangkok','kuil','kuitansi','kuku','kulit','kulkas','kuman','kumuh','kumulatif','kunci','kuning','kupu-kupu','kurang ajar','kurang baik','kursi','kutu','kutu rambut','laba','labah-labah','laboratorium','ladang','lagu','lalai','lambang','lambat','lambung','lampion','lampu','lancar','langit','lapangan','lapar','lapuk','laser','latihan','laut','lawatan','lebah','lega','legenda','leher','lelah','lelucon','lemah','lemak','lemas','lembek','lembut','lendir','lengan','lentera','lentur','lepra','lesbian','lesu','lezat','liburan','lidah','lilin','limbah','limpa','limusin','lincah','lingkaran','lingkungan','lipas','logam','lokakarya','loker','longsor','loteng','lotere','loyal','luar angkasa','luar biasa','lucu','luka','lulusan','lumbung','lumpur','lumut','lunak','mabuk','madu','mahasiswa','mahkota','mainan','majalah','makam','makan','makan malam','makanan','mal','malaikat','malaria','malas','malu','mampu','manajemen','manajer','mandek','mandi','mangkel','mangkuk','maniak','manis','manja','manusiawi','marah','margin','marmut','mars','martabat','masa','masakan','masjid','massa','masturbasi','mata','matahari','matang','matematika','materiil','mati','mayat','meja','melangkah','melawan','melepuh','melodi','melukai','melukis','melunakkan','melupakan','memalukan','memamah ','memamah biak','memanggang','mematuhi','membakar','membayangkan','membelai','membenci','memberkati','membuang','membusuk','memecah','memelihara','memeluk','memendam','memijat','memimpikan','memompa','memotong','memperlakukan','mempesona','memuakkan','memualkan','memukau','memukul','memutilasi','menahan','menampar','menangis','menanti','menara','menarik','mencaci','mencampakkan','mencapit','menceraikan','menciptakan','mencium','mencolek','mencubit','mendarat','mendendam','mendengki','mendung','menebak','menendang','menenggelamkan','mengabaikan','mengabdikan','mengajar','mengaktifkan','mengamankan','mengawal','mengayuh','mengecat','mengecewakan','mengedipkan','mengejek','mengeluhkan','mengembang','mengendalikan','mengerikan','mengerti','mengetik','mengganggu','menggantung','menggapai','menggaruk','menggemaskan','menggetarkan ','menggiling','menggoda','menggunting','menghalangi','menghancurkan','menghanguskan','menghias','menghina ','menghindar','menghormati','mengigit','mengilhami','menginginkan','menginspirasi','mengkhianati','mengobati','mengotori','mengucilkan','menikam','meningkatkan','menjangkau','menjengkelkan','menjerit','menjijikkan','menonton','menopang','mentah','menteri','menulis','menumis','menyakiti','menyalibkan','menyambar','menyampaikan','menyapa','menyayangkan','menyelamatkan','menyembuhkan','menyembunyikan','menyemprot','menyenangkan','menyesali','menyesatkan','menyetrika','menyiksa','menyinggung','menyukai','menyusul','merah','meramu','merantau','merapat','merawat','mercu suar','merdeka','meresapi','meriam','merpati','merusak','mesin','mesra','metode','mewah','militer','mimpi','mimpi buruk','minat','minuman','minyak tanah','mistik','mobil','mobilitas','modar','monyet','moral','motel','muak','mual','muda','mudah','mulut','muntah','muram','murka','murni','murung','museum','musik','musim gugur','musim semi','muslihat','mutasi','nafsu','naik darah','naik pitam','nama','nanah','napas','narkotik','nasi','natal','negara','nektar','neraka','nestapa','neurotik','ngambek','ngeri','nyaman','nyamuk','nyeri','nyiur','obat','obesitas','obsesi','olok-olok','ombak','omong kosong','opini','opsi','optimisme','orang','orang-orang','orgasme','orkestra','otak','pabrik','pacar','pai','pakaian','palsu','palu','palung','paman','pamflet','panah','panda','panik','panitia','pantai','pantat','panter','papan','paradigma','parah','parfum','parlemen','partai','partai','partisipasi','pasal','pasangan','pasar','pasien','pasir','pasta','patah hati','paten','patriot','patung','paus','paviliun','payung','pedas','pejabat','pekat','pekerjaan','pelacur','pelan','pelangi','pelari','pelayaran','pelipis','peluang','peluit','peluk','pelukan','peluru','pemain','pemakaman','pembantai','pembantaian','pembelot','pemberontakan','pembunuh','pembunuhan','pemenggal','pemerasan','pemerintah','pemilu','pemimpin','pemuda','pemuka','penalti','penalti','penari','pencabut nyawa','pencakar langit','pencandu','pencukur','penculikan','pencundang','pencuri','penderitaan','pendeta','pendidikan','penduduk','penerimaan','pengacau','pengadilan','pengamat','pengaruh','pengecut','pengemis','pengering ','pengetahuan','penggawa','penghapus','penghargaan','penghujatan','pengkhianat','pengki','pengrusakan','penguburan','penipuan','penis','penistaan','penjaga','penjahat','penjara','penolakan','pensil','penulis','penyakit','penyalahgunaan','penyegar','penyelam','penyelamat','penyelamatan','penyelia','penyepelean','penyerangan','penyerbu','penyerbuan','penyesalan','penyiksaan','perabot','perahu layar','perampok','peranan','perang','peranti','perasaan','peraturan','perawan','perawat','perban','percaya','percaya diri','perdamaian','perekam','perempuan','perenang','pergelangan','pergi','perilaku','peristiwa','perjalanan','perkakas','perkasa','perkawinan','perkosaan','perlindungan','permainan','permata','permen','pernyataan','persegi','persoalan','pertanian','pertanyaan','perut','pesawat','pesenam','pesisir','pesona','pesta','peti mati','petinju','petir','petualangan','petugas','piala','piaraan','pidana','pikiran','pilihan','pilu','pintu','pipa','pipi','pirang','pisau','pistol','piton','planet','pohon','polisi','polos','pondok','pos','poster','praktik','praktikum','preman','presiden','prestasi','pria','prihatin','privasi','produk','produktif','profit','promosi','protes','provinsi','puas','puisi','pulau','pulpen','puntung','pupuk','pusar','pusing','putih','puting','putra','putri','putus ','putus asa','rabies','racun','radiator','radio','radioaktif','raja','ramah','rapi','rasa','ratu','rawa','rayap','razia','redam','referendum','reformasi','remuk','rendah','rendah hati','rendang','reptil','resah','resep','restoran','reuni','revolusi','revolver','riang','rileks','rinci','rindu','ring','rintangan','risau','risiko','roket','romantis','rompi','rongsokan','ruang','ruangan','rumah','rumah sakit','rumput','rusak','rusuh','saat','sabar','safir','sakit ','sakit gigi','sakit hati','sakit kepala','salad','salah','salam','saleh','salju','sampah','samudera','sandera','sanggama','santo','sapi','saputangan','saraf','sari','sarjana','sate','satelit','satpam','satuan','saudara','saus','sawah','sayang','sayur','sebal','sederhana','sedih','segitiga','sejarah','sekarat','sekolah','seks','seksi','sel','selera','selingkuh','semangat','sembahyang','semesta','senam','senang','senapan','sendiri','sendu','senewen','sengit','seni','senja','senjata','sentimen','senyawa','sepakbola','sepi','sepupu','serangga','serigala','seringai','serius','serong','sertifikat','sesal','setan','setia','sia-sia','siang','sibuk','siku','simpati','simpul','sinar','singa','sinis','sinting','sipilis','sirkus','sistematis','skandal','skeptis','sok','sombong','sosial','spanduk','spidol','stadion','stasiun','stres','suap','sudut','suguhan','suka','sukacita','sukarela','sukaria','sukses','sumbat','sundal','sungai','sup','supel','supermarket','suram','surat','surga','survei','susah ','susu','sutra','tabah','tabrakan','tahu','tajam','tak acuh','takjub','taksi','takut','takzim','tali','taman','tampan','tamparan','tanah','tanah air','tanaman','tangan','tangga','tangkas','tangki','tank','tarif','taring','taufan','tawa','tawanan','tawon','tegang','tekanan','telanjang','telat','telepon','teluk','telur','teman','tembakan','tembakau','tempat','tempe','tempo','tendangan','tenggelam','tengik','tengkorak','tenis','tentara','tenteram','teori','tepuk tangan','terangsang','terbenam','terbit','terbuai','terganggu','terhibur','terinspirasi','terkejut','terkenal','terkepung','terkesan','terkesiap','terluka','termometer','terompet','teroris','terperanjat','terpesona','terpikat','terpisah','tersentuh','tersinggung','tersipu','tertarik','tertekan','terwelu','tetek','tidur','tikus','tim','tinju','tinta','tirai','toko','tolol','tompel','tong','tongkat kruk','topan','topi','tornado','tradisi','tragedi','trauma','truk','tua','tubuh','tuhan','tulus','tumor','tunai','tungku','uang','udara','ulama','ulang tahun','ular','undang-undang','urusan','usia','usil','usus','utang','vagina','vampir','vandal','vila','visi','wajah','waktu','walikota','wanita','warna','wartawan','warung','waspada','waswas','yakin','yoga']

@app.route('/home', methods=['GET', 'POST'])
def home():
    form = TokenListForm()
    if form.validate_on_submit():
        limit = int(form.limit.data)
        objects = []
        list = []
        i = 0
        for word in w2cSorted:
            i = i+1
            tuple = (str(i),word,str(model.wv.vocab[word].count))
            if word in anew:
                objects.append(tuple)
            else:
                list.append(tuple)
            if i >= limit:
                break
        return render_template('index.html', title='Index', form=form, objects=objects, list=list)

    return render_template('index.html', title='Index', form=form)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = SimilarityForm()
    tokens = []
    posts = Post.query.filter_by(user_id=current_user.get_id()).all()
    for p in posts:
        tokens.append(p.chosen_token)
    if form.validate_on_submit():
        results = model.most_similar(form.token.data, topn=int(form.limit.data))
        objects = []
        list = []
        i = 0
        for k, v in results:
            i = i+1
            tuple = (str(i),k,str(v),str(model.wv.vocab[k].count))
            if k in anew:
                objects.append(tuple)
            else:
                list.append(tuple)                
        if 'submit' in request.form:
            vars = request.form.getlist("vars")
            values = request.form.getlist("values")
            for token in vars:
                if token in values:
                    if token not in tokens:
                        u = User.query.get(current_user.get_id())
                        p = Post(search_token=form.token.data, chosen_token = token, author=u)
                        db.session.add(p)
                        db.session.commit()
                        tokens.append(token)
                else:
                    if token in tokens:
                        p = Post.query.filter_by(user_id=current_user.get_id(), chosen_token=token).first()
                        db.session.delete(p)
                        db.session.commit()
                        tokens.remove(token)
        return render_template('home.html', title='Home', form=form, objects=objects, list=list, tokens=tokens)
    return render_template('home.html',  title='Home', form=form, tokens=tokens)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
