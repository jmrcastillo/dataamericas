// import { select, json, tsv, geoPath, geoNaturalEarth1 } from 'd3';
// import { feature } from 'topojson';
const svg = select('svg');
const projection = geoNaturalEarth1();
const pathGenerator = geoPath().projection(projection);

svg.append('path')
    .attr('class', 'sphere')
    .attr('d', pathGenerator({ type: 'Sphere' }));

Promise.all([
    tsv('https://unpkg.com/world-atlas@1.1.4/world/110m.tsv'),
    json('https://unpkg.com/world-atlas@1.1.4/world/110m.json')
]).then(([tsvData, topoJSONdata]) => {
    const countryName = {};
    tsvData.forEach(d => {
        countryName[d.iso_n3] = d.name;
    });

    const countries = feature(topoJSONdata, topoJSONdata.objects.countries);
    svg.selectAll('path').data(countries.features)
        .enter().append('path')
        .attr('class', 'country')
        .attr('d', pathGenerator)
        .append('title')
        .text(d => countryName[d.id]);
});