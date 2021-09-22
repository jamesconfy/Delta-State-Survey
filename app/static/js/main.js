var cityByCategory = {
    Abia: ["Aba", "Umuahia"],
    Adamawa: ["Yola", "Mubi", "Jimeta"],                  
    Akwa_Ibom: ["Uyo", "Ikot Ekpene"],
    Anambra: ["Awka", "Onitsha", "Okpoko"],
    Bauchi: ["Bauchi"],
    Bayelsa: [],
    Benue: ["Makurdi", "Gboko", "Otukpo"],
    Borno: ["Maiduguri", "Kukawa", "Bama"],
    Cross_River: ["Calabar", "Ugep"],
    Delta: ["Warri", "Sapele", "Asaba"],
    Ebonyi: ["Abakaliki"],
    Edo: ["Benin City", "Uromi"],
    Ekiti: ["Ado Ekiti", "Ise Ekiti", "Ilawe Ekiti", "Ijero"],
    Enugu: ["Enugu", "Nsukka"],
    Gombe: ["Gombe"],
    Imo: ["Owerri", "Okigwe"],
    Jigawa: ["Garki"],
    Kaduna: ["Kaduna", "Zaria"],
    Kano: ["Kano"],
    Katsina: ["Katsina", "Funtua"],
    Kebbi: [],
    Kogi: ["Okene"],
    Kwara: ["Ilorin"],
    Lagos: ["Ikorodu", "Ikeja", "Badagry", "Epe"],
    Nasarawa: ["Lafia"],
    Niger: ["Minna", "Mokwa", "Suleja", "Lavun", "Bida"],
    Ogun: ["Abeokuta", "Sagamu", "Obafemi Owode", "Ijebu Ode"],
    Ondo: ["Akure", "Ondo City", "Owo", "Ikare"],
    Osun: ["Ife", "Ilesa", "Iwo", "Osogbo", "Ila", "Gbongan"],
    Oyo: ["Ibadan", "Oyo", "Ogbomosho", "Iseyin", "Shaki", "Kisi", "Igboho"],
    Plateau: ["Jos"],
    Rivers: ["Port Harcourt", "Buguma"],
    Sokoto: ["Sokoto"],
    Taraba: ["Jalingo"],
    Yobe: ["Potiskum", "Gashua"],
    Zamfara: ["Gusau"],
    Abuja: ["Federal Capital Territory"]
}

function changecat(value) {
    if (value.length == 0) document.getElementById("city_options").innerHTML = "<option></option>";
    else {
        var catOptions = "";
        for (categoryId in cityByCategory[value]) {
            catOptions += "<option>"  + cityByCategory[value][categoryId] + "</option>";
        }
        document.getElementById("city_options").innerHTML = catOptions;
    }
}
